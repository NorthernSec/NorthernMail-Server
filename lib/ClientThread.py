#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Client Thread
# Handles connections with the server in separate threads, alowing
#  multiple connections at once.
#
# Copyright (c) 2015	NorthernSec
# Copyright (c) 2015	Pieter-Jan Moreels

# Imports
import socket
import threading

from lib.RSALogger import RSALogger

class ClientThread(threading.Thread):
  def __init__(self,ip,port,clientsocket):
    threading.Thread.__init__(self)
    self.ip=ip
    self.port=port
    self.csocket=clientsocket
    self.logger=RSALogger()

  def run(self):
    try:
      self.logger.log('Accepting connection from %s:%s'%(self.ip,self.port),1)
      data='temp'
      while True and len(data)>0:
        data=self.csocket.recv(2048)
        #handle data
    finally:
      self.logger.log('Closing connection from %s:%s, sending last data'%(self.ip,self.port))
      self.csocket.shutdown(socket.SHUT_RDWR)
      self.logger.log('Closed connection from %s:%s'%(self.ip,self.port),1)
