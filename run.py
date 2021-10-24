#!/usr/bin/env python3.6

from credential import Credential

#functions for user_account


def create_user(fname, lname, phone, email):
  '''
  Function to create a new user
  '''
  new_user = User(fname, lname, phone, email)
  return new_user
