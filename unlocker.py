import subprocess
import serial
import time
class Unlocker:
    def __init__(self):
        self.card = 299630633 #configure this according to the uid you want to be accepted
        self.port = serial.Serial("/dev/ttyACM0",1000000) #configure this according to your microcontroller directory and its baudrate
    def compare(self):
        print(f"Connected to {self.port.name}")
        while True:
            line = self.port.readline() #reads line from port
            line = line.decode().strip() #leaves the pure string
            line = int(line)
            if line == self.card:
                self.acc = True
                break
            else:
                self.acc = False
                break
        self.port.close()
    def unlock(self):
        if self.acc == True:
            print("Card was recognized successfully!")
            process = subprocess.Popen(["loginctl unlock-session 3"],shell=True) #configure this with your own user session ID
        else:
            print("Card was not recognized")
if __name__ == "__main__": #checks if program is ran as file instead of being imported
    proc = Unlocker()
    while True:
        proc = Unlocker()
        time.sleep(1)
        proc.compare()
        proc.unlock()
