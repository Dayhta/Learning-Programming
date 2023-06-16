import paramiko
import os
import socket

class SSHServer(paramiko.ServerInterface):
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY.PROHIBITED
    def check_auth_password(sefl, usersname, password):
        if (usersname == 'sshuser') and (password == 'sshpass'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
    

def main():
    server = '0.0.0.0'
    port = 2222
    CWD = os.getcwd()
    HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'id_rsa'))
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(server, port)
        sock.listen()
        