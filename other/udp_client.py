import socket
from typing import Tuple

IP = "127.0.0.1"
PORT = 20001
BUFFER_SIZE = 1024

DEFAULT_MESSAGE = "Hello, UDP server!"


def send_udp_packet(msg: str = DEFAULT_MESSAGE) -> Tuple[bytes, Tuple[str, int]]:
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client_socket.sendto(msg.encode('utf-8'), (IP, PORT))
    return udp_client_socket.recvfrom(BUFFER_SIZE)


def main() -> None:
    try:
        print("Full server data packet:", send_udp_packet())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
