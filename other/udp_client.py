import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Tuple, Generator

IP = "127.0.0.1"
PORT = 20001
BUFFER_SIZE = 1024

DEFAULT_MESSAGE = "Hello, UDP server!"


def send_udp_packet(msg: str = DEFAULT_MESSAGE) -> Tuple[bytes, Tuple[str, int]]:
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client_socket.sendto(msg.encode('utf-8'), (IP, PORT))
    return udp_client_socket.recvfrom(BUFFER_SIZE)


def spawn_concurrent_udp_packets(num: int = 10) -> Generator:
    with ThreadPoolExecutor(max_workers=num) as executor:
        for i in range(num):
            yield executor.submit(send_udp_packet, str(i))


def main() -> None:
    try:
        for future in as_completed(spawn_concurrent_udp_packets()):
            print("Full server data packet:", future.result())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
