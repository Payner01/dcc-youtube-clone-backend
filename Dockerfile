FROM python:alpine
ENV PYTHONNUMBUFFERED 1
WORKDIR /app
COPY requirements.txt requirments.txt
RUN pip3 install -r requirments.txt
COPY . . 