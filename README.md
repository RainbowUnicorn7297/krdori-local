# krdori-local
BanG Dream! Korean Version (뱅드림! 걸즈 밴드 파티! / 한도리) Local Server

Currently supports all stories, including Main Story, Band Story and Event Story up to the penultimate event "To Those Who Will Depart (떠나는 사람에게)."

Planned features:
- Event Story for the last event "Welcome! Joyous New Year! (영춘 만세! 경사스러운 새해!)"
- Free Live
- Edit Band

If you want to request a specific feature that is not supported, please feel free to open a new [issue](https://github.com/RainbowUnicorn7297/krdori-local/issues).

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

More technical details can be found [here](README-technical.md).
