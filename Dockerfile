FROM python:3

RUN \
apt-get update -y && \
apt-get install python3-pip -y

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD [ "python3","testRunner.py" ]