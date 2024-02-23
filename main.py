from krdori.servers.game_server import app

# Port used by the game server
_game_port = 8482

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=_game_port, debug=False)
