import subprocess
import serial
import time
class Unlocker:
    def __init__(self):
        self.card = 299630633 #configure this according to the uid you want to be accepted
        self.port = serial.Serial("/dev/ttyACM0",1000000) #configure this according to your microcontroller directory and its baudrate
        self.acc = None
        self.session = 3 #configure this with your own session ID
        print(f"Connected to {self.port.name}")
    def compare(self):
        while True:
            line = self.port.readline() #reads line from port
            line = line.decode().strip() #leaves the pure string
            try:
                line = int(line)
            except ValueError:
                print("Error! Microcontroller picked up malformed data!")
            else:
                if line == self.card:
                    self.acc = True
                    break
                else:
                    self.acc = False
                    break
    def unlock(self):
        if self.acc == True:
            print("Card was recognized successfully!")
            process = subprocess.Popen([f"loginctl unlock-session {self.session}"],shell=True)
        elif self.acc == False:
            print("Card was not recognized")
        else:
            print("Error! No card detected")
if __name__ == "__main__": #checks if program is ran as file instead of being imported
    proc = Unlocker()
    while True:
        try:
            proc.compare()
            time.sleep(1)
            proc.unlock()
        except KeyboardInterrupt:
            print("\n"+"Program Closed")
            break
