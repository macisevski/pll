import bottle
from api import pile, letter, line

app = application = bottle.WaitressServer()

if __name__ == '__main__':
    bottle.run(host='127.0.0.1', port=8000)
