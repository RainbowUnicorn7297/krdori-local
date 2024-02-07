"""Game API server"""

from concurrent import futures
import logging

import grpc

from takasho.schema.common_featureset.player_api import ondemand_master

# Port used by the Kakao SDK server
_port = 50051


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    ondemand_master.add_OndemandMasterServicer_to_server(
        ondemand_master.OndemandMaster(), server)

    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f'Server started, listening on {port}')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve(_port)

