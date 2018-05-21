from flask import Flask
import socket
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello BUTTHEAD!"

@app.route('/server')
def getServer():
    hostname = socket.gethostname();
    return hostname

if __name__ == '__main__':
    app.run()
