#!/usr/local/bin/python3.7

import sys
import os
import signal
import socket
from scapy.all import Packet, wrpcap

LOG_INTERVAL = 100

if __name__ == '__main__':
	
	if len(sys.argv) <= 2:
		print("Usage: {} <interface> <output_filename>".format(os.path.basename(__file__)))
		sys.exit(1)

	iface = sys.argv[1]
	output_file = sys.argv[2]

	print("Sniffer started on interface {}...".format(iface))
	print("Press CTRL+C to stop sniffing.\n")

	with open(output_file, 'w') as f:
		f.write('')

	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
	s.bind((iface, 3))

	packets = []
	i = 0

	def signal_trap(sig, frame):
		''' theoretically, interrupt could malform last packet '''
		for pkt in packets[:-1]:
			wrpcap(output_file, pkt, append=True)

		print("\nProgram stopped. Packets saved to {}.".format(output_file))
		sys.exit(0)

	signal.signal(signal.SIGINT, signal_trap)

	while True:
		raw_pkt = s.recvfrom(1500)[0]
		packets += Packet(raw_pkt)

		''' print every log in one line '''
		print("\r", end="")
		print("{} packets captured ".format(i), end="")
		sys.stdout.flush()

		i += 1