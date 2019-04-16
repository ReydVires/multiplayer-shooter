import socket
from _thread import *
from player import Player
import pickle

IP = 'localhost'  # This server IP
PORT = 9901
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind((IP, PORT))
except socket.error as e:
    str(e)
sock.listen(2)

print("Server Started, waiting for a connection...")
current_player = 0
players = [
    Player(0, 225, 50, 50, 50, (140, 20, 252)),  # obj Player1
    Player(1, 225, 400, 50, 50, (107, 185, 240), -1)  # obj Player2
]


def threaded_client(connection, player_num):
    # TODO: Check Play after 2 client connected
    # TODO: Handling if 1 is disconnected
    # TODO: Restart game
    # TODO: Another game with ID
    # thread for individual client behavior
    connection.send(pickle.dumps(players[player_num]))
    while True:
        try:
            data = pickle.loads(connection.recv(1024))
            if not data:
                print("Disconnected")
                break
            else:
                #  if player 1 then pos [0] otherwise [1]
                players[player_num] = data
                if player_num == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received:", data)
                print("Debug: player {}, hp {}".format(player_num, reply.health))
            print("Sending:", reply)
            connection.sendall(pickle.dumps(reply))
        except error:
            break
    print("Lost connection")
    connection.close()


while True:
    conn, addr = sock.accept()
    print('Total current player is {}'.format(current_player))
    print("Connected to", addr)
    start_new_thread(threaded_client, (conn, current_player,))
    current_player += 1  # everytime player/client added, player sum up
