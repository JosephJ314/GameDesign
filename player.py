import zmq
servID = "127.0.0.1"
ctx = zmq.Context()
soc = ctx.socket(zmq.REQ)
soc.connect("tcp://%s:9801"%servID)
soc.send(open(input("Player information file: "),"rb").read())
res = soc.recv(1024).decode("UTF-8")
sock = ctx.socket(zmq.PAIR)
sock.connect("tcp://%s:%s"%(servID,res))
while True:
    sock.send(input(sock.recv(1024).decode("UTF-8")))