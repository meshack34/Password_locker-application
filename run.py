#!/usr/bin/env python3.6

from credential import Credential
from user import User

def create_user(firstname, lastname, phonenumber, email):
  ''' new user '''
  mynew_user = User(firstname, lastname, phonenumber, email)
  return mynew_user
