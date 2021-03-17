FROM selenium/standalone-firefox

USER root
WORKDIR /src
COPY requirements.txt /src/
RUN apt-get update -y && apt install -y python3-pip python-dev build-essential
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /src/

