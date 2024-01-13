import socket


def SendMsg():
    # 클라이언트가 보내고자 하는 서버의 IP와 PORT
    server_ip = "10.10.15.102"
    server_port = 3000
    server_addr_port = (server_ip, server_port)

    #보낼 메세지를 byte 배열로 변경
    msg_from_client = "발사"
    bytes_to_send = str.encode(msg_from_client)

    #소켓을 UDP로 열고 서버의 IP/Port로 메세지를 보낸다
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client_socket.sendto(bytes_to_send, server_addr_port)
    print(msg_from_client)
