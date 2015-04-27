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
    self.AESKey=None
  def run(self):
    try:
      self.logger.log('Accepting connection from %s:%s'%(self.ip,self.port),1)
      data='temp'
      while True and len(data)>0:
        data=self.csocket.recv(2048)
        response=handleData(data)
        if response:
          csocket.send(encrypt(response))
    finally:
      self.logger.log('Closing connection from %s:%s, sending last data'%(self.ip,self.port))
      self.csocket.shutdown(socket.SHUT_RDWR)
      self.logger.log('Closed connection from %s:%s'%(self.ip,self.port),1)

  def encrypt(data):
    if self.AESKey:
      #TODO: handle encryption
      print("Encryption to do")
    data=data.encode('utf-8')
    return data

  def handleData(data):
    d=data.upper()
    if d.startswith("FETCH"):
      #TODO: handle mails
      return "Placeholder for mails"
