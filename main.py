from krdori.servers.game_server import app

_port = 5000

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=_port, debug=False)
