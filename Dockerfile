FROM dockerfile/java:openjdk-7-jre

MAINTAINER Oliver Lade <piemaster21@gmail.com>
# See https://github.com/NetLogo/NetLogo/wiki/Controlling-API

# Install system dependencies.
RUN apt-get update
RUN apt-get install -qq wget python

RUN wget https://ccl.northwestern.edu/netlogo/5.1.0/netlogo-5.1.0.tar.gz
RUN tar xzf netlogo-5.1.0.tar.gz && rm netlogo-5.1.0.tar.gz
RUN mv netlogo-5.1.0 /opt/netlogo

# Copy the API directory across.
ADD api /api
