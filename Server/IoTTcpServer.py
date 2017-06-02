"""
  IoTTcpServer.py
  MyIoT_Server

  Created by Bob Chen on 02/06/2017.
"""

from socketserver import TCPServer, BaseRequestHandler
from IoTBaseServer import IoTBaseServer


class IoTTcpServer(IoTBaseServer):
    'TtpServer'

    def __init__(self, ip, port):

        self._tcpServer = TCPServer((ip, port), IoTTcpServerHandler)

    def start(self):
        pass

    def stop(self):
        pass


class IoTTcpServerHandler(BaseRequestHandler):
    'TcpServerHandler'
    pass
