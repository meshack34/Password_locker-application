#!/usr/bin/env python3.6

from credential import Credential
from user import User

def mynew_user(firstname, lastname, phonenumber, email):
  ''' new user '''
  mynew_user = User(firstname, lastname, phonenumber, email)
  return mynew_user


def save_mynew_user(user):
  '''
  Function to save user
  '''
  user.save_user()


def delete_mynew_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()
