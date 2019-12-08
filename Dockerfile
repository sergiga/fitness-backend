FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/gymbackend
WORKDIR /opt/gymbackend
COPY requirements.txt /opt/gymbackend
RUN pip install -r requirements.txt
COPY . /opt/gymbackend