FROM python:3

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FILEIT_POSTGRES_USER fileit
ENV FILEIT_POSTGRES_PASSWORD password
ENV FILEIT_POSTGRES_DB fileit
ENV FILEIT_POSTGRES_HOST db

COPY . . 

CMD ["sh", "startscript.sh"]
