import socket
url=input("Enter")
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
con=url.split("/")
try:
    addr=con[2]
except:
    print("error not in right format")
    quit()
mysock.connect((addr,80))
cmd='GET'+' '+url+ ' ' +'HTTP/1.0\r\n\r\n'
cmd=cmd.encode()
mysock.send(cmd)
while True:
    data=mysock.recv(500)
    if len(data)<1:
        break
    print(data.decode())
