import subprocess
import serial
import time
class Unlocker:
    def __init__(self):
        self.card = "299630633" #configure this
        self.port = serial.Serial("/dev/ttyACM0",1000000,timeout=1) #configure this
    def compare(self):
        time.sleep(1)
        print(f"Connected to {self.port.name}")
        while True:
            line = self.port.readline()
            line = line.decode().strip()
            if line == self.card:
                self.acc = True
                break
            else:
                self.acc = False
                break
        self.port.close()
    def unlock(self):
        if self.acc == True:
            print(1)
        else:
            print(0)
if __name__ == "__main__": #checks if program is ran as file instead of being imported
    while True:
        proc = Unlocker()
        time.sleep(1)
        proc.compare()
        proc.unlock()

