FROM python:3

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV IMAGEIT_POSTGRES_USER imageit
ENV IMAGEIT_POSTGRES_PASSWORD password
ENV IMAGEIT_POSTGRES_DB imageit
ENV IMAGEIT_POSTGRES_HOST db

ENV IMAGEIT_API_KEY secret 

COPY . . 

CMD ["sh", "startscript.sh"]
