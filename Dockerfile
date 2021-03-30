FROM python:3

RUN useradd -m gpu_crawler
ENV USER=gpu_crawler

WORKDIR /home/$USER

COPY requirements.txt /home/$USER

RUN apt-get update -y && apt-get install -y python3-pip python-dev build-essential
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /home/$USER

USER gpu_crawler

