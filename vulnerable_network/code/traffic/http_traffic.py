#!/usr/bin/python3.6

import requests
import random
import time

if __name__ == '__main__':
	urls = [
		'https://www.pw.edu.pl',
		'http://www.elka.pw.edu.pl',
		'http://studia.elka.pw.edu.pl',
		'http://studia.elka.pw.edu.pl/cal/',
		'http://home.elka.pw.edu.pl/~jolszak2/',
		'https://usosweb.usos.pw.edu.pl'
		]

	while True:
		time.sleep(random.randint(0, 120))
		url = random.choice(urls)
		try:
			requests.get(url)
		except:
			print("WARN: {} may be not accessible".format(url))
