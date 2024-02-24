#!/data/data/com.termux/files/usr/bin/bash

if [ -d ./krdori-local ]; then
    cd krdori-local
    git pull https://github.com/RainbowUnicorn7297/krdori-local.git
    source env/bin/activate
elif [ -d ../krdori-local ]; then
    git pull https://github.com/RainbowUnicorn7297/krdori-local.git
    source env/bin/activate
else
    yes | pkg upg
    yes | pkg ins git
    yes | pkg ins python
    git clone https://github.com/RainbowUnicorn7297/krdori-local.git
    cd krdori-local
    python -m venv env
    source env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install websockets
    python -m pip install protobuf
    python -m pip install pycryptodome
    python -m pip install flask
fi
python main.py &
