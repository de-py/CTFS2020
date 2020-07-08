import socket



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.182.198', 1337))
    # s.send('test')
    data = s.recv(1024)
    print('Received', repr(data))
    # 360c1f0605360c1e
    # 0c0c10361b041a08
    # s.send(b"\x08\x1a\x04\x1b\x36\x10\x0c\x0c\x1e\x0c\x36\x05\x06\x1f\x0c\x36")
    # s.send(b"\x1e\x0c\x36\x05\x06\x1f\x0c\x36\x08\x1a\x04\x1b\x36\x10\x0c\x0c")
    # s.send(b"\x36\x0c\x1f\xf0\x60\x53\x0c\x1e\x0c\x0c\x10\x36\x1b\x04\x1a\x08")
    s.send(b"\x0c\x0c\x10\x36\x1b\x04\x1a\x08\x36\x0c\x1f\xf0\x60\x53\x0c\x1e\x0a")

    data = s.recv(1024)
    print('Received', repr(data))



if __name__ == "__main__":
    main()