FROM similitude/netlogo-docker

MAINTAINER Oliver Lade <piemaster21@gmail.com>
# See https://github.com/NetLogo/NetLogo/wiki/Controlling-API

# Install system dependencies.
RUN apt-get update && apt-get install -qq python python-lxml

# Copy the API directory across.
ADD api /api

