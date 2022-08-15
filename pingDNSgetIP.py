#! /usr/bin/env python3

# Стояла задача найти ip адресса по dns именам

import json
import os
import subprocess

filein = '../servers.json'
fileout = 'serversoutput.txt'

with open(filein, 'r') as serv:
	templates = json.load(serv)
	for row in templates:
		print(row['dns'])
		with open(fileout, 'a') as file:
			try:
				print(subprocess.check_output(["ping", "-c 1", row['dns']]))
				print('\n\n')
				file.write('\n'+row['dns']+'\n')
				file.write('\n'+subprocess.check_output(["ping", "-c 1", row['dns']]).decode("utf-8"))
			except subprocess.CalledProcessError as e:
				print(row['dns'] + ' has no ip')
				file.write('\n' + row['dns'] + ' has no ip UWU\n')
