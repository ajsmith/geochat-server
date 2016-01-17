FROM fedora:23

MAINTAINER Alex Smith <alex.smith@redhat.com>

RUN dnf install -y python-virtualenv python-psycopg2 geos-python && dnf clean all

ADD . /opt/geochat-server
WORKDIR /opt/geochat-server
RUN ./install.sh
WORKDIR /var/lib/geochat
USER geochat

EXPOSE 8080
ENTRYPOINT ["/opt/geochat-server/run_geochatd.sh"]
