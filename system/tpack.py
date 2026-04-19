import struct

class TPack:
	# Packet formats
	HANDSHAKE_FMT = ">HBBBHBBH"
	HAT_DATA_FMT = ">HBBBHhhhhhh"
	PANTS_DATA_FMT = ">HBBBHhhhhhhB"

	# Packet header and ID
	HEADER = 0xF668
	ID : int = 0x0000
	CHARACTER_ID : int = 0x00
	WHERE : int = 0x00

	# Packing methods
	@classmethod
	def pack_handshake(cls, connected: bytes):
		return struct.pack(cls.HANDSHAKE_FMT, cls.HEADER, cls.WHERE, cls.CHARACTER_ID, 0x01, cls.ID, connected, b'\x01' if cls.ID != b'\x00\x00' else b'\x00', cls.ID if cls.WHERE == b'\x01' else b'\x00\x00')
	@classmethod
	def pack_hat_data(cls, pos: tuple):
		return struct.pack(cls.HAT_DATA_FMT, cls.HEADER, cls.WHERE, cls.CHARACTER_ID, 0x00, cls.ID, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])
	@classmethod
	def pack_pants_data(cls,  pos: tuple, buttons: bytes):
		return struct.pack(cls.PANTS_DATA_FMT, cls.HEADER, cls.WHERE, cls.CHARACTER_ID, 0x00, cls.ID, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], buttons)
	
	# Unpacking methods
	@classmethod
	def auto_unpack(cls, data):
		length = len(data)
		if length == struct.calcsize(cls.HANDSHAKE_FMT):
			return cls.unpack_handshake(data)
		elif length == struct.calcsize(cls.PANTS_DATA_FMT):
			return cls.unpack_pants_data(data)
		elif length == struct.calcsize(cls.HAT_DATA_FMT):
			return cls.unpack_hat_data(data)
		
	@classmethod
	def unpack_handshake(cls, data):
		return struct.unpack(cls.HANDSHAKE_FMT, data)	
	@classmethod
	def unpack_hat_data(cls, data):
		return struct.unpack(cls.HAT_DATA_FMT, data)
	@classmethod
	def unpack_pants_data(cls, data):
		return struct.unpack(cls.PANTS_DATA_FMT, data)
