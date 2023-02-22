FROM python:3.9

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./expecific_middleware .

CMD [ "python", "app.py" ]