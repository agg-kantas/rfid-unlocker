# RFID Unlocker

## What it does
Taps an RFID card near an RC522 reader (connected to a Raspberry Pi Pico 2W) to unlock a locked Linux session

## Workflow
- Rasperry Pi scans for RFID tags using Anti-Collision and selects their UID's
- Converts the UID's into an integer and prints them over USB serial
- A python daemon on the host's machine reads the UID's and compares them against an authorized card
- If it matches, the daemon runs a command to unlock the current user's session

## Hardware Requirements
- Any Raspberry Pi Pico version
- RC522 RFID Reader Module

## Software Requirements
- Python 3 with pyserial installed
- MicroPython on the Pico (unless you're using a different microcontroller)
- Linux disro with systemd and loginctl

### Possible Alternatives
- **Microcontroller:** ESP32/ESP8266/Arduino
- **RFID Module:** PN532/RDM6300

### Wiring (RC522 > Pico)
|RC522 Pin |Pico Pin|
|---|---|
|3.3V      |3V3     |
|GND       |GND     |
|SCK       |GP2     |
|MOSI      |GP3     |
|MISO      |GP4     |
|RST       |GP0     |
|SDA/CS    |GP1     |

>Do not power the RC522 module with 5V, otherwise you risk damaging it

## Installation

### Pico side (MicroPython)
Copy `pico/mfrc522.py` and `pico/main.py` onto the Pico (through an IDE like Thonny), and run the `main.py` script so it runs automatically on boot.
**Make sure your IDE is closed before you use the daemon because it can throw a multiple ports open error**

### Host side (Debian/Linux)
```bash
git clone https://github.com/agg-kantas/rfid-unlocker.git
cd rfid-unlocker/daemon
pip install pyserial --break-system-packages
```
**(On SOME Linux Distros pyserial might already be installed as a package, it would be wise to check before installing it with pip)**

Edit `unlocker.py` and set:
- `self.card` > the UID of your authorized tag (check it by what the Pico script prints out on scan)
- `self.port` > your serial device path (usually /dev/ttyACM0) and baudrate of your reader module (leave it as is if you're using RC522)
- `self.session` > your loginctl session ID (use loginctl list-sessions to check)

Run `unlocker.py` as a systemd service (daemon)
```bash
sudo cp rfid-unlocker.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable rfid-unlocker.service
sudo systemctl start rfid-unlocker.service
```

Check daemon status using ```systemctl status rfid-unlocker.service```

##What I learned


## Notes
This unlocks an already logged in, locked session. It does NOT replace your login password, nor does it act as a PAM authentication factor. The password stored on the machine is never touched, this project strictly uses Bash commands to simply unlock the desired session.
