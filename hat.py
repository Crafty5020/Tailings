print("INITIALIZING HAT")
from system.tpack import TPack
from main import id, character_id, where
import system.radioManager as rM



def main():
	global id, character_id, where
	rM.hat_init()
	

