########
# This image will compile the dependencies
# It will install compilers and other packages, that won't be carried
# over to the runtime image
########
# FROM alpine:3.12.4 AS compile-image
FROM python:rc-slim-buster AS compile-image

# create the main dit
RUN  mkdir -p opt/code

# RUN mkdir -p /opt/code
WORKDIR /opt/code

# promition - working dir
RUN chmod -R 777 /opt/code

# install pip
RUN apt update -y && apt install python3-pip -y

# Create a virtual environment for all the Python dependencies
RUN python3 -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

# for fast build
RUN pip install --upgrade pip setuptools wheel

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the code(dont need that - will do in the next image)
# COPY . .

# promition - THE END
RUN chmod -R 777 /opt/code

# ########
# # This image is the runtime, will copy the dependencies from the other
# ########
FROM python:rc-slim-buster AS runtime-image

# create the bin dir
RUN  mkdir -p /opt/venv

# promition opt
RUN chmod -R 777 /opt

# Copy the venv with compile dependencies from the compile-image
COPY --from=compile-image /opt/venv /opt/venv

# Be sure to activate the venv
ENV PATH="/opt/venv/bin:$PATH"

# create the main dir
RUN  mkdir -p /opt/code

# making working dir
WORKDIR /opt/code

# promition - working dir
RUN chmod -R 777 /opt/code

# copy the content of the local src directory to the working directory
COPY . .

# envirment variable for controoling from ymal
ENV DEBUG_MODE="real"

# promition END
RUN chmod -R 777 /opt/code



# envirment variable - no need: controlling from ymal
# ENV HOST_LOW_AREA=svc-python-area-low.p-2022-91.svc.cluster.local PORT_LOW_AREA=8012
# ENV HOST_HIGH_AREA=svc-python-area-high.p-2022-91.svc.cluster.local PORT_HIGH_AREA=8022
# ENV HOST_ATTACKER=svc-python-attacker.p-2022-91.svc.cluster.local PORT_ATTACKER=8014
# ENV HOST_SERVER=svc-python-analysis-server.p-2022-91.svc.cluster.local PORT_SERVER=8030

# open port from the contanier
EXPOSE 8014

# run the sms-server-grpc
CMD ["/bin/sh","-c", "python3 main.py"]

# scp -r C:\bgu\p-2022-091\Attacker a87@192.168.0.61:/p-2022-091/storage/nfs/image_build
# docker build -t python-attacker:v0.3 /p-2022-091/storage/nfs/image_build/Attacker/

# push to local registry:
# docker tag python-attacker:v0.3 192.168.0.235:5000/python-attacker:latest
# docker push 192.168.0.235:5000/python-attacker:latest



# docker run:
# docker run --name python-attacker -d -p 8012:8012 192.168.0.235:5000/python-attacker:latest
# docker image ls
# inspact the containing:
# docker ps -a
# sudo docker logs python-attacker
# sudo docker inspect python-attacker
# docker exec -it -u root python-attacker /bin/sh
# docker exec -it python-attacker /bin/sh

# find the images:
# docker images 192.168.0.235:5000/python-attacker

# remove docker contaner and image:
# docker container stop python-attacker
# docker rm -f $(docker ps -aq)
# docker image rm -f $(docker image ls python-attacker -q)
# docker rm -f attacker-python
# docker image rm -f python-attacker
# docker image ls | grep python-attacker
# docker image rm -f <container> <container> <container>