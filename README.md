# krdori-local
BanG Dream! Korean Version Local Server

Technical details can be found [here](README-technical.md).

## Quick Start
1. Download and install [this modded game APK](https://mega.nz/file/rMB10RRL#ff7M5xGRW08GsuEUlBBmdEtmkhSrs-Z0S4u-UHY2FOQ) on your Android device.
2. Download and install [Termux](https://f-droid.org/repo/com.termux_118.apk) on your Android device.
3. Open Termux and run these commands to download and run [krdori.sh](krdori.sh):
```
curl https://bit.ly/krdori -o krdori.sh -L
chmod +x krdori.sh
./krdori.sh
```
The game should be playable by now.

To stop the local server from running, use the `pkill python` command.

## Required Python Packages
- websockets
- protobuf
- pycryptodome
- flask
