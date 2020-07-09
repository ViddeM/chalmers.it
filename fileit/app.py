import os
import uuid
import config
from datetime import datetime

from flask import Flask, flash, request, redirect, url_for, send_from_directory
from pony.orm import Database, PrimaryKey, Required, db_session, select, Optional

db = Database()
db.bind(
    provider='postgres',
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    port=config.POSTGRES_PORT,
    database=config.POSTGRES_DB
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.FILE_SAVE_FOLDER
app.config['MAX_CONTENT_LENGTH'] = config.FILE_SIZE_CAP_BYTES

if not os.path.exists(config.FILE_SAVE_FOLDER):
    raise (Exception('Directory not found: "%s"\n'
                     'Create the directory or change "config.py"' % config.FILE_SAVE_FOLDER))


class File(db.Entity):
    fileid = PrimaryKey(uuid.UUID, auto=True)
    filelink = Required(str)
    uploadtime = Optional(datetime)


db.generate_mapping(create_tables=True)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # verify api key
        if config.API_KEY != request.headers["API_KEY"]:
            return "Invalid API key"

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            with db_session:
                file = File(
                    filelink="somelink/link.png",
                )
                id = file.fileid
                file_directory = app.config['UPLOAD_FOLDER'] + "/" + str(id) + "/"

                if not os.path.exists(file_directory):
                    os.makedirs(file_directory)

                file.filelink = file_directory + file.filename
                file.save(os.path.join(file_directory, file.filename))
            return url_for('uploaded_file', imageid=file.fileid, filename=file.filename)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type="text" name="API_KEY">
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<fileid>/<filename>')
def uploaded_file(fileid, filename):
    file_directory = app.config['UPLOAD_FOLDER'] + "/" + fileid + "/"
    return send_from_directory(file_directory, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
