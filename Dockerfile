FROM python:3.9

COPY . /

RUN pip3 install -r requirements.txt

EXPOSE 5000