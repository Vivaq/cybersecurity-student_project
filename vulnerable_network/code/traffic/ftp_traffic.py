#!/usr/bin/python3.6

from ftplib import FTP
import random
import time
import sys

if __name__ == '__main__':

	ftp = FTP('192.168.2.4')
	ftp.login()
	ftp_commands = [
		(ftp.retrlines, 'LIST'), 
		(ftp.sendcmd, 'HELP'), 
		(ftp.sendcmd, 'PWD'),
		(ftp.sendcmd, 'STAT'),
		(ftp.sendcmd, 'SYST'),
		(ftp.retrbinary, 'RETR abc', open('cba', 'wb').write)
	]

	while True:
		time.sleep(random.randint(0, 60))
		fun, *command = random.choice(ftp_commands)
		fun(*command)
