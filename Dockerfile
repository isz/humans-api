FROM python:3.8

RUN pip install pipenv \
    && pip install gunicorn \
    && mkdir -p /var/local/human_api/media

WORKDIR /usr/local/humans_api
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system
COPY manage.py .
COPY humans_api ./humans_api

EXPOSE 8000
CMD ["gunicorn","-w", "3", "-b", "0.0.0.0:8000", "humans_api.wsgi"]
