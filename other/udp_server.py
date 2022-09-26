import socket

IP = "127.0.0.1"
PORT = 20001
BUFFER_SIZE = 1024

DEFAULT_MESSAGE = "Hello, UDP client!"


def bind_udp_server_socket() -> socket.socket:
    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_server_socket.bind((IP, PORT))
    print("UDP server up and listening")
    return udp_server_socket


def run_udp_server(udp_server_socket: socket.socket, msg: str = DEFAULT_MESSAGE):
    while True:
        bytes_address_pair = udp_server_socket.recvfrom(BUFFER_SIZE)
        message = bytes_address_pair[0]
        address = bytes_address_pair[1]

        print("Message from client: {}".format(message))
        print("Client IP address: {}".format(address))

        udp_server_socket.sendto(msg.encode('utf-8'), address)


def main() -> None:
    sock = bind_udp_server_socket()
    try:
        run_udp_server(sock)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
