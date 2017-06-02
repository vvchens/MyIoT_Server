"""
  IoTHttpServer.py
  MyIoT_Server

  Created by Bob Chen on 02/06/2017.
"""

from flask import Flask
from IoTBaseServer import IoTBaseServer


class IoTHttpServer(IoTBaseServer):
    'HttpServer'

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port

    def start(self):
        app = Flask(__name__)

        @app.route("/")
        def hello():
            return "Hello World!"

        app.run(self._ip, self._port)

    def stop(self):
        pass


if __name__ == "__main__":
    IoTHttpServer('0.0.0.0', 80).start()
