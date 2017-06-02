"""
  IoTUdpServer.py
  MyIoT_Server

  Created by Bob Chen on 02/06/2017.
"""

from socketserver import UDPServer, BaseRequestHandler
from IoTBaseServer import IoTBaseServer


class IoTUdpServer(IoTBaseServer):
    'UdpServer'

    def __init__(self, ip, port):

        self._udpServer = UDPServer((ip, port), IoTUdpServerHandler)

    def start(self):
        pass

    def stop(self):
        pass


class IoTUdpServerHandler(BaseRequestHandler):
    'UdpServerHandler'
    pass
