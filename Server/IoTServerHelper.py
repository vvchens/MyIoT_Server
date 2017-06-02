"""
  IoTServerHelper.py
  MyIoT_Server

  Created by Bob Chen on 02/06/2017.
"""

from IoTHttpServer import IoTHttpServer
from IoTTcpServer import IoTTcpServer
from IoTUdpServer import IoTUdpServer

IP = '0.0.0.0'
HTTPPORT = 80
TCPPORT = 3333
UDPPORT = 3333


class IoTServerHelper:
    'IoTServerHelper'

    def __init__(self):
        self._httpServer = IoTHttpServer(IP, HTTPPORT)
        self._tcpServer = IoTTcpServer(IP, TCPPORT)
        self._udpServer = IoTUdpServer(IP, UDPPORT)

    def start(self):
        'start'
        self._httpServer.start()


if __name__ == "__main__":
    IoTServerHelper().start()
