__license__ = "CC BY-NC-ND 4.0"
__version__ = "0.1.0"

import random
import struct
from system.tpack import TPack

# ID, Character ID, and Where are initialized in main_init.py and assigned to TPack class variables
id : bytes = b'\x00\x00'
character_id : bytes = b'\x00'
where : bytes = b'\x00'

def init():
	global id, character_id, where
	try:
		# Get character id AND where (Binary Version)
		with open('CHARACTER.tconf', "a+b") as f:
			f.seek(0) # Ensure we're at the start of the file
			content = f.read()
			print(f"CHARACTER.tconf content: {content}") 
			if len(content) < 2:
				print("CHARACTER.tconf is too small!")
				raise ValueError("CHARACTER.tconf must be 2 bytes (CharID + Where)")
			else:
				# Direct byte access
				f.peek(0)  # Ensure we're at the start
				character_id = struct.unpack('>BB', content)[0]  # Read 1 byte for character_id
				f.peek(0)
				where = struct.unpack('>BB', content)[1]  # Read 1 byte for where

				print(f"CHARACTER ID found: {hex(int(character_id))}, WHERE found: {hex(int(where))}")
	except OSError:
		print("CHARACTER.tconf not found. Create it in Thonny!")
	
	if where == 1:
		print("WHERE is set to HAT. Starting hat main loop.")
		import hat
		hat_init()
		hat.main()
	else:
		print("WHERE is set to pants. Starting pants main loop.")
		import pants
		pants.init()

	# 3. Assign to TPack class
	TPack.CHARACTER_ID = int(character_id)
	TPack.WHERE = int(where)
	TPack.ID = int(id)

def hat_init() -> bytes:
	global id
	# 1. Handle ID.conf (Binary Mode)
	try:
		with open('ID.tconf', "a+b") as f:
			f.seek(0) # Ensure we're at the start of the file
			content = f.read().strip()
			print(f"ID.tconf content: {content}")
			if content == b'':
				print("ID.tconf is empty. Generating random ID!")
				# Generate 2 random bytes and convert to a 16-bit integer for TPack.ID (H)
				random_bytes = random.getrandbits(16).to_bytes(2, 'big')
				f.seek(0)
				f.write(random_bytes)
				id = struct.unpack('>H', random_bytes)[0]
			else:
				# Unpack the 2-byte binary ID from the file to an integer
				id = struct.unpack('>H', content)[0]
				print(f"ID found: {hex(int(id))}")
	except OSError:
		print("ID.tconf not found. Create it in Thonny!")
	
	return id

	print("Starting Pants main loop")
if __name__ == "__main__":
	init()