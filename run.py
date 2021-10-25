#!/usr/bin/env python3.6

from credential import Credential
from user import User
import math
import random


def mynew_user(firstname, lastname, username, phonenumber, email):
  ''' new user '''
  mynew_user = User(firstname, lastname,username, phonenumber, email)
  return mynew_user


def newuser_save(user):
  '''Function to save user'''
  user.newuser_save()


def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_myuser()


def copyuser_mail(user, phonenumber):
  '''
  Function to delete a user
  '''
  user.copyuser_mail(phonenumber)


def find_user(phonenumber):
  '''
  finds a user by phonenumber and returns the user
  '''
  return User.find_by_phoneNumber(phonenumber)


def check_existing_user(phonenumber):
  '''
  Function that check if user exists with phonenumber and returns a Boolean
  '''
  return User.checkuser_exist(phonenumber)


def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_myusers()




#The user credential details
def create_credential(credential_userName, password, phonenumber, credential_email):
  '''
  Function to create a new credential
  '''
  new_credential = Credential(credential_userName, password, phonenumber, credential_email)
  return new_credential


def save_credential(credential):
  '''
  save credential
  '''
  credential.save_credential()


def del_credential(credential):
  '''
  delete a credential
  '''
  credential.delete_credentials()


def copy_pwd(credential, phonenumber):
  '''
  Function to delete a credential
  '''
  credential.copymypasswod(phonenumber)


def find_credential(phonenumber):
  '''
  Function that finds a credential by phonenumber and returns the credential
  '''
  return Credential.find_by_phoneNumber(phonenumber)


def check_existing_credential(phonenumber):
  '''
  Function that check if credential exists with phonenumber and returns a Boolean
  '''
  return Credential.checkcredential_exist(phonenumber)


def display_credentials():
  '''
  Function that returns all the saved credentials
  '''
  return Credential.display_credentials()

