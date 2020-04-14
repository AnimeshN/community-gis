FROM python:3.7.6-stretch
MAINTAINER GeoNode development team

RUN mkdir -p /usr/src/my_geonode

# Enable postgresql-client-11.2
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -


# This section is borrowed from the official Django image but adds GDAL and others
RUN apt-get update && apt-get install -y \
		gcc \
                zip \
		gettext \
		postgresql-client-11 libpq-dev \
		sqlite3 \
                python3-gdal python3-psycopg2 \
                python3-pil python3-lxml \
                python3-dev libgdal-dev \
                libmemcached-dev libsasl2-dev zlib1g-dev \
                python3-pylibmc \
                uwsgi uwsgi-plugin-python3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*


RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y geoip-bin

# add bower and grunt command
COPY . /usr/src/my_geonode/
WORKDIR /usr/src/my_geonode

RUN apt-get update && apt-get -y install cron
COPY monitoring-cron /etc/cron.d/monitoring-cron
RUN chmod 0644 /etc/cron.d/monitoring-cron
RUN crontab /etc/cron.d/monitoring-cron
RUN touch /var/log/cron.log
RUN service cron start

COPY wait-for-databases.sh /usr/bin/wait-for-databases
RUN chmod +x /usr/bin/wait-for-databases
RUN chmod +x /usr/src/my_geonode/tasks.py \
    && chmod +x /usr/src/my_geonode/entrypoint.sh

# Upgrade pip
RUN pip install pip --upgrade

# app-specific requirements
RUN pip install --upgrade --no-cache-dir --src /usr/src -r requirements.txt
RUN pip install --upgrade -e .

# Install pygdal (after requirements for numpy 1.16)
RUN pip install pygdal==$(gdal-config --version).*

ENTRYPOINT service cron restart && /usr/src/my_geonode/entrypoint.sh
