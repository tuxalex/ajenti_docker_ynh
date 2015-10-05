#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
from docker import Client

app=sys.argv[1]
containername=sys.argv[2]

#Get the hostname
hostname = socket.gethostname()
imagename = hostname+'/'+app

#Connect to docker socket
cli = Client(base_url='unix://docker.sock')

print("Start remove container")
details=cli.inspect_container(container=containername)
#First print IP, then print redirect port, finaly print not redirect ports
print(","+details['NetworkSettings']['IPAddress']
      +","+details['NetworkSettings']['Ports']['8000/tcp'][0]['HostPort'])

#Stop and remove container
cli.stop(container=containername)
cli.remove_container(container=containername, force=True)

#Remove docker image
cli.remove_image(image=imagename, force=True)

exit()

