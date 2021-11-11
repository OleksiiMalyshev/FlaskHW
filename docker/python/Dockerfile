FROM python:3.8.12

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt
COPY wait-for-it.sh wait-for-it.sh

RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt

CMD python3 app.py