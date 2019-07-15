#!/usr/local/bin/python2.7

import random
import time
import os

if __name__ == '__main__':
	ip_addrs= [
		'182.170.1.1',
		'182.170.2.1',
		'182.170.3.1',
		'192.168.2.2',
		'192.168.2.3',
		'192.168.2.4',
		'192.168.2.5'
	]
	
	while True:
		time.sleep(random.randint(0, 30))
		ip = random.choice(ip_addrs)

		os.system('ping -c 3 {}'.format(ip))
