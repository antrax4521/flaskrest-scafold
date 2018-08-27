FROM python:3.6

ENV SRC /app
ENV PORT 8099
ENV APPNAME "FLASK"
ENV API_KEY cb8ea0df409c19e994958f72751fc2fe
ENV TOKEN_SECRET 103427e0-7715-0136-8b74-0026b6e97153
ENV DATABASE_URL postgres://user:password@host:5432/database
ENV REDIS_URL redis://@host:18629/index


RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nginx
RUN mkdir $SRC $SRC/logs

COPY config/site.conf /etc/nginx/sites-available/
COPY config/entry-point.sh /
RUN chmod +x /entry-point.sh && chmod 700 /entry-point.sh

RUN ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

WORKDIR $SRC
VOLUME [ "$SRC/logs" ]

COPY . $SRC

RUN pip3 install -r $SRC/requirements.txt

EXPOSE 8099

ENTRYPOINT ["/entry-point.sh"]
