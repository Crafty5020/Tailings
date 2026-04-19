from system.tpack import TPack
from pyrf24 import RF24, RF24_PA_LOW

def hat_init():
    print("Initializing Radio Manager")
    # This is where we would set up the radio communication, e.g. using a library
    radio = RF24(22, 0) # CE=GPIO22, CSN=GPIO8 (CE0)
    if not radio.begin():
        raise RuntimeError("Radio hardware not responding")

    radio.set_pa_level(RF24_PA_LOW)
    # Match your Pico's address (5 bytes)
    address = b"PTnow" 
    radio.open_rx_pipe(1, address)
    radio.start_listening()

    while True:
        if radio.available():
            length = radio.get_dynamic_payload_size()
            raw_data = radio.read(length)
            print(f"Raw data received: {raw_data}")
            # Use your TPack class here!
            result = TPack.auto_unpack(raw_data)
            print(f"Received: {result}")





