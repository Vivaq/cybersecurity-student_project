#!/usr/bin/python3.6

from smtplib import SMTP
import time
import random
import sys

if __name__ == '__main__':

	with SMTP('182.170.2.2') as smtp:

		smtp_commands = [smtp.noop, smtp.helo, smtp.ehlo]
		while True:
			time.sleep(random.randint(0, 90))
			random.choice(smtp_commands)()
