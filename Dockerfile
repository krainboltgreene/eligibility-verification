FROM python:3.8.5
ARG PORT
ENV PORT ${PORT}

EXPOSE ${PORT}

ARG DOCKER_DIR
WORKDIR ${DOCKER_DIR}

ARG DOCKER_USER

RUN useradd ${DOCKER_USER} && \
    chown -R ${DOCKER_USER}:${DOCKER_USER} ${DOCKER_DIR}

USER ${DOCKER_USER}

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
