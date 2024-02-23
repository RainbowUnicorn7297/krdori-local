# krdori-local
BanG Dream! Korean Version Local Server

Technical details can be found [here](README-technical.md).

## Quick Start
1. Download and install [this modded game APK](https://mega.nz/file/XJpA1ITT#65UCLON5ZUk0xaLXFFAcjJ8rbiFS1DoWv-PUx_-vhSA) on your Android device.
2. Download and install [Termux](https://f-droid.org/repo/com.termux_118.apk) on your Android device.
3. Open Termux and run these commands:
```
pkg upg
pkg in git
pkg in python
git clone https://github.com/RainbowUnicorn7297/krdori-local.git
cd krdori-local
python -m venv env
source env/bin/activate
python -m pip install --upgrade pip
python -m pip install websockets
python -m pip install protobuf
python -m pip install pycryptodome
python -m pip install flask
python krdori/servers/kakao_server.py &
python krdori/servers/session_server.py &
python main.py &
```
The game should be playable by now.

On newer versions of Android, clicking on the "Log in with Kakao Account" button launches a browser that shows an `about:blank` page without redirecting back to the game. You can visit the link `http://127.0.0.1:8480/oauth/authorize` using another browser to bypass this.

## Required Python Packages
- websockets
- protobuf
- pycryptodome
- flask
