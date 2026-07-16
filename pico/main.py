from mfrc522 import MFRC522
import time
reader = MFRC522(sck=2,mosi=3,miso=4,rst=0,cs=1)
reader.init()
while True:
    stat,bits = reader.request(reader.REQIDL)
    if stat==reader.OK: # checks if its picking up a card
        stat,uid = reader.SelectTagSN()
        if stat==reader.OK: # checks if it selected a tag correctly
            uid_bytes = bytes(uid) #converts uid to bytes
            card = int.from_bytes(uid_bytes,"little",False) #converts bytes in little Endian order, unassigned, to an integer
            print(card)
            time.sleep(0.5)