import board
import busio
import digitalio
import struct
from circuitpython_nrf24l01.rf24 import RF24
import system.tpack as TPack

def init():
	# Setup SPI and control pins
	spi = busio.SPI(board.GP6, MOSI=board.GP4, MISO=board.GP7)
	ce = digitalio.DigitalInOut(board.GP17)
	csn = digitalio.DigitalInOut(board.GP14)

	# Initialize the radio module
	nrf = RF24(spi, csn, ce)

	# Set addresses (must match on both radios)
	address = [b"1Node", b"2Node"]
	nrf.open_tx_pipe(address[0])
	nrf.open_rx_pipe(1, address[1])

	while True:
		if nrf.available():
			payload = nrf.recv()
			length = len(payload)
			
			if length == 11:
				print("Connection handshake received!")
				# Logic to verify the 11-byte flag...
			elif length == 18:
				print("Standard command received from Hat.")
				# Logic for tail movement...
				
			# Prepare the 19-byte response for the NEXT time the Hat pings
			pant_tpack = struct.pack("19s", b"PANT_DATA_19_BYTES")
			nrf.load_ack(1, pant_tpack)

def main():
	pass