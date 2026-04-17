import struct

class TPack:
	# Packet formats
	HANDSHAKE_FMT = ">HBBBHB"
	HAT_DATA_FMT = ">HBBBHhhhhhh"
	PANTS_DATA_FMT = ">HBBBHhhhhhhB"

	# Packet header and ID
	HEADER : bytes = b'\xF6\x68'
	ID : bytes = b'\x00\x00'
	CHARACTER_ID : bytes = b'\x00'
	WHERE : bytes = b'\x00'

	# Packing methods
	@classmethod
	def pack_handshake(cls, connected: bytes):
		return struct.pack(cls.HANDSHAKE_FMT, cls.HEADER, cls.WHERE, cls.CHARACTER_ID, 0x01, cls.ID, connected)
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
