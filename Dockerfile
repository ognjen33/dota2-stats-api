FROM python:3.8-alpine

RUN mkdir dota2_service

WORKDIR '/dota2_service'

COPY requirements.txt /dota2_service
RUN pip3 install -r requirements.txt

COPY . /dota2_service

CMD [ "python3", "-u", "app.py"]