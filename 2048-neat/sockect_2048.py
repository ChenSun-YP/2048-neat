import socket
import time
import json
from game.utils import Direction
from game.utils import State
from game.utils import Key

# constants
port = 2048
segment_size = 2048
hostname = "localhost"
default_game_size = 4

# vars
state = State.MENU
status = None

s = None


def initialize():
    global s
    # IPv4, TCP Stream
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(hostname)
    print(ip)
    s.connect((ip, port))
    print("Successfully connected on %s" % ip)


def restart_game(size):
    size = default_game_size if 3 <= size <= 9 else size
    if state != State.MENU:
        _send(Key.BACK)

    _send(size)
    _send(Key.ENTER)
    _recv()


def make_move(direction):
    if direction == Direction.UP:
        _send(Key.UP)
    elif direction == Direction.DOWN:
        _send(Key.DOWN)
    elif direction == Direction.LEFT:
        _send(Key.LEFT)
    elif direction == Direction.RIGHT:
        _send(Key.RIGHT)

    _recv()
    return _get_game()


# Retrieves the board from connection
def _recv():
    global status
    global state
    status = json.loads(s.recv(segment_size))
    state = status['gameState']
    for i, ki in enumerate(status):
        print(str(i) + ": " + str(ki))


def _get_game():
    return status


def _send(message):
    if type(message) is Key:
        message = message.value

    message = str(message)
    print("Sending: " + message)
    s.send(message.encode('utf-8')) #+ b'\r\n'
    s.send(b'\r\n')


# _send(4)
# _recv()
# _send(Key.UP)
# _recv()
# _send(Key.LEFT)
# _recv()
# Uses shutdown to gracefully close the socket
# Most applications disregard this and uses close straight away
# s.shutdown(socket.SHUT_RDWR)
# s.close()
