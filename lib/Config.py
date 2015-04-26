#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
#
# Config reader to read the configuration file
#
# Copyright (c) 2015	NorthernSec
# Copyright (c) 2015	Pieter-Jan Moreels
#
# Software is free software released under the "Original BSD license"

# imports
import sys
import os
runPath = os.path.dirname(os.path.realpath(__file__))
import configparser

class Configuration():
  confParse=configparser.ConfigParser()
  confParse.read(os.path.join(runPath, "../etc/config.ini"))
  default={'host':'localhost', 'port':5002, 'logging':True,
           'logPath':'../log/NorthernMail.log', 'verbose':True,
           'logLevel':0, 'verboseLevel':0}

  @classmethod
  def readSetting(cls,section,item,default):
    try:
      if type(default)==bool:
        return cls.confParse.getboolean(section,item)
      elif type(default)==int:
        return cls.confParse.getint(section,item)
      else:
        return cls.confParse.get(section,item)
    except:
      return default

  # Server settings
  @classmethod
  def getHost(cls):
    return cls.readSetting('Server', 'Host', cls.default['host'])

  @classmethod
  def getPort(cls):
    return cls.readSetting('Server', 'Port', cls.default['port'])

  # Logging
  @classmethod
  def logging(cls):
    return cls.readSetting('Logging', 'Enabled', cls.default['logging'])

  @classmethod
  def logPath(cls):
    return cls.readSetting('Logging', 'Path', cls.default['logPath'])

  @classmethod
  def logLevel(cls):
    return cls.readSetting('Logging', 'logLevel', cls.default['logLevel'])

  @classmethod
  def verbose(cls):
    return cls.readSetting('Logging', 'Verbose', cls.default['verbose'])

  @classmethod
  def verboseLevel(cls):
    return cls.readSetting('Logging', 'VerboseLevel', cls.default['verboseLevel'])

