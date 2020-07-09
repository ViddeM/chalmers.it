from flask import Flask, send_from_directory, request, flash, redirect, url_for, make_response, render_template, \
    send_file
from flask_restful import Resource, Api

import config
import db_handler

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.FILE_SAVE_FOLDER
app.config['MAX_CONTENT_LENGTH'] = config.FILE_SIZE_CAP_BYTES
app.secret_key = 'super secret key'
api = Api(app)


class UploadFileRes(Resource):

    def get(self):
        return make_response(render_template("upload.html"))

    def post(self):
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
        if file:
            file_id = db_handler.store_file_in_db(file)
            return str(file_id)


class RetrieveFileRes(Resource):
    def get(self, file_id: str):
        file_directory = db_handler.retrieve_file_link(file_id)
        return send_file(file_directory)


api.add_resource(RetrieveFileRes, "/api/file/<string:file_id>")
api.add_resource(UploadFileRes, "/api/upload")


def run():
    app.run(host='0.0.0.0')
