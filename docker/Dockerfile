FROM fedora:23

MAINTAINER Alex Smith <alex.smith@redhat.com>

RUN dnf install -y python-virtualenv python-psycopg2 geos-python && dnf clean all

RUN useradd geochat -u 1000 -d /var/lib/geochat
ADD . /var/lib/geochat/py
RUN chown -R geochat:geochat /var/lib/geochat

WORKDIR /var/lib/geochat/py

USER geochat
RUN ./install.sh

WORKDIR /var/lib/geochat

EXPOSE 8080
ENTRYPOINT ["/var/lib/geochat/py/run_geochatd.sh"]
