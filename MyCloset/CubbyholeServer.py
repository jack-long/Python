#! /usr/bin/env python
"""This is a cubbyhole server.

The following commands are supported by this Cubbyhole:

PUT <message>  -  Places a new message in the cubbyhole
GET            -  Takes the message out of the cubbyhole and displays it
LOOK           -  Displays the massage without taking it out of the cubbyhole
DROP           -  Takes the message out of the cubbyhole without displaying it
HELP           -  Displays this help message
QUIT           -  Terminates the connection
"""
import SocketServer
import socket

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    message = "<no message stored>"
    def handle(self):
        self.request.settimeout(10.0)
        connection = True
        while(connection):
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024)
                # recv returns '' when the client closes the connection
                if not self.data:
                    break
            except socket.timeout:
                 break
            
            data = self.data.strip()
            data = data.split(' ')
            command = data[0].upper()
            new_message = data[1] if len(data) > 1 else ""
            # if command empty
            
            feedback = "!" + command + ": "
            if command == "QUIT":
                feedback += "ok"
                connection = False
            elif command == "LOOK":
                feedback += self.message
            elif command == "PUT":
                self.message = new_message
                feedback += "ok"
            elif command == "GET":
                feedback += self.message
                self.message = "<no message stored>"
            elif command == "DROP":
                self.message = ""
                feedback += "ok"
            elif command == "HELP":
                feedback += """
The following commands are supported by this Cubbyhole:

PUT <message>  -  Places a new message in the cubbyhole
GET            -  Takes the message out of the cubbyhole and displays it
LOOK           -  Displays the massage without taking it out of the cubbyhole
DROP           -  Takes the message out of the cubbyhole without displaying it
HELP           -  Displays this help message
QUIT           -  Terminates the connection"""
            else:
                feedback += "Invalid command. "
            feedback += "\n> " 
            print "{} wrote:".format(self.client_address[0]), command, new_message
            # just send back the same data, but upper-cased
            self.request.sendall(feedback)

if __name__ == "__main__":
    HOST, PORT = "localhost", 1337

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
