FROM registry.access.redhat.com/ubi8/python-36
WORKDIR /opt/app-root/src

COPY . /opt/app-root/src/
RUN pip install -r requirements.txt
CMD ./start.sh
