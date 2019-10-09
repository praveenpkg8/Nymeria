FROM ubuntu:16.04
RUN apt-get update -y
RUN  apt-get -y install python3-dev python3-pip \
        && pip3 install --upgrade pip
COPY . /app
WORKDIR /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["twitter_bot.py"]

