FROM ubuntu:latest
LABEL authors="slav"

ENTRYPOINT ["top", "-b"]