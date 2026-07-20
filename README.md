# RFID Unlocker

## What it does
Taps an RFID card near an RC522 reader (connected to a Raspberry Pi Pico 2W) to unlock a locked Linux session

## Workflow
- Rasperry Pi scans for RFID tags using Anti-Collision and selects their UID's
- Converts the UID's into an integer and prints them over USB serial
- A python daemon on the host's machine reads the UID's and compares them against an authorized card
- If it matches, the daemon runs a command to unlock the current user's session
