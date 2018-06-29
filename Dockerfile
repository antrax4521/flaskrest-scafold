FROM python:3.6.4

WORKDIR /var/www/flaskrest
COPY . /var/www/flaskrest

RUN pip3 install -r requirements.txt

ENV APPNAME FLASKREST
ENV WEB_CONCURRENCY 100
ENV PORT 9000
ENV API_KEY cb8ea0df409c19e994958f72751fc2fe
ENV DATABASE_URL postgres://localhost:5432/postgres

EXPOSE 9000

VOLUME [ "/var/www/flaskrest" ]
CMD [ "gunicorn", "--bind", "0.0.0.0:9000", "app:app" ]