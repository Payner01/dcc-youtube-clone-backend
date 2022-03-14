FROM python:alpine

ENV PYTHONNUMBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
ADD ./ /app



# RUN pip install -r requirements.txt
RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER  appuser
CMD [ "python", "drf_jwt_backend/manage.py", "runserver", "0.0.0.0:8000" ]
