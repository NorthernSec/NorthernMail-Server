#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Server for the Darknet NorthernSec Mail project

# Copyright (c) 2015	NorthernSec
# Copyright (c) 2015	Pieter-Jan Moreels
# This software is licensed under the Original BSD License

# Imports
import argparse
import signal
import socket

from lib.ClientThread import ClientThread
from lib.Config import Configuration as conf
from lib.RSALogger import RSALogger

# Constants
VERSION='pre-release'
RELEASEDATE='pre-release'
DESC='''Server for the NorthernSec darknet mailing project.'''

# Parse args
parser = argparse.ArgumentParser(description=DESC)
parser.add_argument('-v', action='store_true', help='Version')
args=parser.parse_args()

# Main 
if __name__=='__main__':
  if args.v:
    print("NorthernMail %s (%s)"%(VERSION,RELEASEDATE))
    sys.exit(0)
  # Retrieve config
  host=conf.getHost()
  port=conf.getPort()
  # Start logging
  logger=RSALogger()

  # Start server
  sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  addr=(host,port)
  logger.log('Starting NorthernMail server %s on %s:%s'%(VERSION,host,port), 1)
  sock.bind(addr)
  sock.listen(1)
  try:
    while True:
      (cl_sock, (cl_ip,cl_port))=sock.accept()
      logger.log(('Starting new thread for connected client - %s:%s'%(cl_ip,cl_port)))
      thread=ClientThread(cl_ip,cl_port,cl_sock)
      thread.start()
  except KeyboardInterrupt:
    logger.log('Shutting down server, sending last data', 0)
    sock.shutdown(socket.SHUT_RDWR)
    logger.log('Server shut down', 1)
