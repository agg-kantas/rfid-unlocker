import subprocess
import serial
class Unlock:
    def __init__(self,card = 299630633): #change the card's correct uid in int form, according to your own
        self.card = card
    def compare(self):
        port = serial.Serial("/dev/ttyACM0",1000000)
if __name__ == "__main__": #checks if program is ran as file instead of being imported
    print("bill")
