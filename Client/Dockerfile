########
# This image will compile the dependencies
# It will install compilers and other packages, that won't be carried
# over to the runtime image
########
# FROM alpine:3.12.4 AS compile-image
FROM python:3.11.0b1-slim-buster AS compile-image

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
FROM python:3.11.0b1-slim-buster AS runtime-image

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
EXPOSE port

# run the sms-server-grpc
CMD ["/bin/sh","-c", "python3 main.py"]
