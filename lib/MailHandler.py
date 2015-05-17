#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Mail Handler
# Handles mail related operations (storing, fetching, etc)
#  ! NOTE: This is a temporary class for development, and stores mails temporarily in /tmp, as an sqlite db !
#
# Copyright (c) 2015    NorthernSec
# Copyright (c) 2015    Pieter-Jan Moreels

# Imports
import json
import sqlite3

TEMPFILE="/tmp/mails.db"


def verifyTable():
  conn=sqlite3.connect(TEMPFILE)
  conn.execute('''CREATE TABLE IF NOT EXISTS  MAILS
                 (ID        INTEGER  PRIMARY KEY AUTOINCREMENT,
                  SUBJECT   TEXT            NOT NULL,
                  MESSAGE   TEXT            NOT NULL,
                  TOKEN     TEXT            NOT NULL,
                  SIGNATURE TEXT);''')
  conn.close()

def addMail(json):
  verifyTable()
  conn=sqlite3.connect(TEMPFILE)
  subj=json['subject'] if 'subject' in json else None
  mess=json['message'] if 'message' in json else None
  sign=json['signature'] if 'signature' in json else None
  token=json['token'] if 'token' in json else None
  conn.execute('''INSERT INTO MAILS(SUBJECT, MESSAGE, SIGNATURE, TOKEN)
                  VALUES(:subj,:mess,:sign, :token)''',
                  {'subj':subj,'mess':mess,'sign':sign,'token':token})
  conn.commit()
  conn.close()

def fetchMails():
  verifyTable()
  conn=sqlite3.connect(TEMPFILE)
  curs=conn.cursor()
  mails = curs.execute('SELECT * FROM MAILS')
  mailArray=[]
  names = list(map(lambda x: x[0], curs.description))
  j={}
  for m in mails:
    for i in range(0,len(names)):
      j[names[i].lower()]=m[i]
    mailArray.append(j)
  conn.close()
  return mailArray
