import zmq
import races
import classes
import threading
import sys
from queue import Queue
ctx = zmq.Context()
main_socket = ctx.socket(zmq.REP)
players = []
MAXPLAYERS = 5
class Player:
    def __init__(self,thd,specs):
        self.thd = thd

class playerhandler(threading.Thread):
    def __init__(self,playerip):
        super().__init__(self)
        self.socket = ctx.socket(zmq.PAIR)
        self.socket.bind("tcp://%s"%playerip)
        self.queue = Queue()
        self.outqueue = Queue()
    def run(self):
        while True:
            self.queue.put(self.socket.recv(1024).decode("UTF-8"))
            try:
                self.socket.send(self.outqueue.get_nowait())
            except:
                self.socket.send("")
print("Starting...")
if len(sys.argv)>1:
    MAXPLAYERS = int(sys.argv[1])
while len(players)<MAXPLAYERS:
    data = main_socket.recv(1024).decode("UTF-8")
    thd = playerhandler(data.split(" ")[0])
    thd.start()
    player = Player(thd," ".join(data.split(" ")[1:]))
    players.append()
while True:
    for player in players:
        intxt = player.queue.get()

