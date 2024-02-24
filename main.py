import asyncio
from multiprocessing import Process

from krdori.servers import game_server, kakao_server, session_server

# Port used by the Kakao SDK server
_kakao_port = 8480
# Port used by the session server
_session_port = 8481
# Port used by the game server
_game_port = 8482


if __name__ == '__main__':
    kakao_process = Process(
        target=kakao_server.start,
        args=(_kakao_port,),
        daemon=True
    )
    kakao_process.start()
    game_process = Process(
        target=game_server.start,
        args=(_game_port,),
        daemon=True)
    game_process.start()

    try:
        asyncio.run(session_server.main(_session_port))
    except KeyboardInterrupt:
        pass

