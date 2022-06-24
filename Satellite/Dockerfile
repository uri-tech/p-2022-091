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
COPY . .

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

# open port from the contanier
# EXPOSE port

# run the sms-server-grpc
CMD ["/bin/sh","-c", "python3 main.py"]


# scp -r C:\bgu\p-2022-091\Satellite a87@87.68.184.164:/p-2022-091/storage/nfs/image_build

# scp -r C:\bgu\p-2022-091\Satellite a87@192.168.0.61:/p-2022-091/storage/nfs/image_build
# docker build -t python-satellite:v0.4 /p-2022-091/storage/nfs/image_build/Satellite/

# push to local registry:
# docker tag python-satellite:v0.4 192.168.0.235:5000/python-satellite:latest
# docker push 192.168.0.235:5000/python-satellite:latest



# docker run:
# docker run --name python-satellite -d -p 8012:8012 192.168.0.235:5000/python-satellite:latest
# docker image ls
# inspact the containing:
# docker ps -a
# sudo docker logs python-satellite
# sudo docker inspect python-satellite
# docker exec -it -u root python-satellite /bin/sh
# docker exec -it python-satellite /bin/sh

# find the images:
# docker images 192.168.0.235:5000/python-satellite

# remove docker contaner and image:
# docker container stop python-satellite
# docker rm -f $(docker ps -aq)
# docker image rm -f $(docker image ls python-satellite -q)
# docker rm -f satellite-python
# docker image rm -f python-satellite
# docker image ls | grep python-satellite
# docker image rm -f <container> <container> <container>

# k:
# kubectl -n p-2022-091 get pods
# kubectl -n p-2022-091 logs deployment-python-satellite-65945dbc76-jxpbn
# kubectl -n p-2022-091 delete pod