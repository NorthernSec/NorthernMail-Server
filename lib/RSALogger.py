#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
#
# Logs events using a public key, for added security. This way system
#  administrators and coders can debug the server, while making sure
#  a high level of privacy is kept, by keeping the logs safe.
#
# Copyright (c) 2015	NorthernSec
# Copyright (c) 2015	Pieter-Jan Moreels
#
# Software is free software released under the "Original BSD license"

# imports
from lib.Config import Configuration as conf
from datetime import datetime as dt

class RSALogger():
  def __init__(self):
    self.verbose=conf.verbose()
    self.logging=conf.logging()
    self.logPath=conf.logPath()
    self.logLevel=conf.logLevel()
    self.verboseLevel=conf.verboseLevel()
    self.levels=["DEBUG", "INFO", "WARN", "ERROR", "CRIT"]
  def log(self, message, sev=0):
    if (self.logging and sev>=self.logLevel) or (self.verbose and sev>=self.verboseLevel):
      now=dt.now().strftime("%d/%m/%Y %H:%M:%S")
      try:
        level=self.levels[sev]
      except Exception as e:
        level="NONE"
      log="%s (%s) %s"%(now,level,message)
      if sev>=self.logLevel:
        #log to disk
        print('will be logged')
      if sev>=self.verboseLevel:
        print(log)
