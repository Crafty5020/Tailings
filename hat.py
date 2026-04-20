print("INITIALIZING HAT")
from system.tpack import TPack
from main import id, character_id, where
import system.hat.radioManager as rM
tcpack = __import__("external.tcpack-parser")



def main():
	global id, character_id, where
	print("Starting HAT main loop")
	

