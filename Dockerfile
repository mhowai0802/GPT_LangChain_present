FROM python:3.11

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update; apt-get clean

RUN apt-get install -y wget

RUN apt-get install -y gnupg

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get -y install google-chrome-stable

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["api.py"]

EXPOSE 5001