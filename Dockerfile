FROM python:3.6

###################################################################################
# INSTALL DEPENDENCIES
###################################################################################

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nginx supervisor

###################################################################################
# CONFIGURE NGINX
###################################################################################

RUN rm /etc/nginx/sites-enabled/default
COPY config/site.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled/site.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

###################################################################################
# CONFIGURE SUPERVISOR
###################################################################################

RUN mkdir -p /var/log/supervisor
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

###################################################################################
# ADD FLASK APP
###################################################################################

RUN mkdir /app
ADD . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

###################################################################################
# ADD ENV VARS
###################################################################################

ENV APPNAME flaskapp
ENV API_KEY 123123123123123123123123123
ENV DATABASE_URL postgres://user:pass@host:5432/database

###################################################################################
# RUN AND EXPOSE THE APP
###################################################################################

EXPOSE 8099

RUN chmod -R 777 /app

CMD [ "sh", "/app/config/entry-point.sh" ]
