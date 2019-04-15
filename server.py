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
    Player(225, 50, 50, 50, (255, 0, 0)),  # obj Player1
    Player(225, 400, 50, 50, (0, 0, 255), -1)  # obj Player2
]


def threaded_client(connection, player_num):
    # thread for individual client behavior
    # TODO: Instead of dir, use id for player_num!
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
                print('DEBUG: player', player_num, "| hp:", reply.health)
            print("Sending:", reply)
            connection.sendall(pickle.dumps(reply))
        except error:
            break
    print("Lost connection")
    connection.close()


while True:
    conn, addr = sock.accept()
    print("Connected to", addr)
    start_new_thread(threaded_client, (conn, current_player,))
    current_player += 1  # everytime player/client added, player sum up
