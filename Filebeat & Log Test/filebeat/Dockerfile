ARG ELK_VERSION
# FROM ubuntu:latest

FROM docker.elastic.co/beats/filebeat:${ELK_VERSION}

#Run filebeat
USER root
RUN apt-get update && apt-get install -y python3-pip

RUN mkdir /home/Logs
RUN mkdir /home/FilebeatLogs
RUN chmod 755 /home/FilebeatLogs
# RUN touch /home/FilebeatLogs/filebeat.log
# COPY generate.py /home/Logs/

COPY init.sh .
RUN chmod +x init.sh
# WORKDIR /home/

# RUN /home/init.sh
# COPY file.log /home/Logs/
# CMD cd /home/Logs
# CMD ["python3", "/home/Logs/generate.py"]
