FROM python:alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUMBUFFERED 1
WORKDIR /app
COPY requirements.txt /django/
RUN pip install -r requirments.txt
COPY . . 