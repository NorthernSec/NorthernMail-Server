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
import json
import socket
import struct
import threading

from lib.RSALogger import RSALogger
import lib.MailHandler as MH

class ClientThread(threading.Thread):
  def __init__(self,ip,port,clientsocket):
    threading.Thread.__init__(self)
    self.ip=ip
    self.port=port
    self.csocket=clientsocket
    self.logger=RSALogger()
    self.AESKey=None

  def encrypt(self,data):
    if self.AESKey:
      #TODO: handle encryption
      print("Encryption to do")
    data=struct.pack("I",len(data))+data.encode('utf-8')
    return data

  def handleData(self,data):
    if not 'command' in data:
      return None
    d=data['command'].upper()
    if d == "FETCH":
      self.logger.log('FETCH from connection %s:%s'%(self.ip,self.port))
      return json.dumps({'mails':MH.fetchMails(), 'response':'success'})
    elif d == "POST":
      self.logger.log('POST from connection %s:%s'%(self.ip,self.port))
      if 'mail' in data:
        MH.addMail(json.loads(data['mail']))
    else:
      self.logger.log('Invalid command (%s) from connection %s:%s'%(d,self.ip,self.port))
    return None


  def run(self):
    try:
      self.logger.log('Accepting connection from %s:%s'%(self.ip,self.port),1)
      data='temp'
      while True and len(data)>0:
        #TODO: define message boundries
        recv=self.csocket.recv(4)
        recv=int.from_bytes(recv,byteorder="big")
        data=b''
        while(len(data)<recv):
          data+=self.csocket.recv(recv)
        try:
          data=data.decode('utf-8')
          data=json.loads(data)
          try:
            response=self.handleData(data)
          except Exception as e:
            print('Exeption during data handling:')
            print(e)
          if response:
            self.csocket.send(self.encrypt(response))
        except:
          print("Bogus data sent:")
          print(data)
          print("===")
          pass
    finally:
      self.logger.log('Closing connection from %s:%s, sending last data'%(self.ip,self.port))
      self.csocket.shutdown(socket.SHUT_RDWR)
      self.logger.log('Closed connection from %s:%s'%(self.ip,self.port),1)
