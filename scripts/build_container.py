#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket
import sys
from docker import Client

app=sys.argv[1]
containername=sys.argv[2]
yunohostid=sys.argv[3]
dockerized=sys.argv[4]

#Get the hostname
hostname = socket.gethostname()
imagename = hostname+'/'+app

#Connect to docker socket
cli = Client(base_url='unix://docker.sock')

#Define port binding
if dockerized:
	config=cli.create_host_config(network_mode='container:'+yunohostid)
else:
	config=cli.create_host_config(port_bindings={8000: ('127.0.0.1',8000)})

#Build docker image with the Dockerfile and disply the output
for line in cli.build(path='../build/', tag=imagename):	
	out=json.loads(line)
	#sys.stdout.write('\r')
	#print(out['stream'])
	#sys.stdout.flush()

#Create the container and display result
container = cli.create_container(
			image=imagename, 
			detach=True,  
			tty=True,
			name=containername,
			host_config=config
)		

#Start the container and display result
cli.start(container=containername)

details=cli.inspect_container(container=containername)
#First print IP, then print redirect port, finaly print not redirect ports
#print(","+details['NetworkSettings']['IPAddress']
#      +","+details['NetworkSettings']['Ports']['8000/tcp'][0]['HostPort'])

exit()

