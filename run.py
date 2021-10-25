#!/usr/bin/env python3.6

from credential import Credential
from user import User
import math
import random


def createnew_user(firstname, lastname, user_name,phonenumber, email):
  ''' new user '''
  mynew_user = User(firstname, lastname, user_name, phonenumber, email)
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
  '''Function to create a new credential
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


def main():
  print("HELLO, WELCOME TO PASSWORD LOCKER \n")
  print("Use these short codes :")
  print("Please chose what to do: \n ca - command to create new account choosing your own password \n auto - command to auto generated password \n x - command to exit the program \n")

  while True:
    short_code = input().lower()

    #user creating own password
    if short_code == 'ca':
      print("New user account")
      print("-"*10)

    print("First name ....")
    f_name = input()

    print("Last name ...")
    l_name = input() 
    print("username ...")
    u_name = input()
    print("Phone number ...")
    p_number = input()
    print("password  ...")
    m_password = input()
    print("Email address ...")
    e_address = input()
    newuser_save(createnew_user(f_name, l_name, u_name, p_number, e_address))
    print('\n')
    print(f"New Contact {f_name} {l_name} created")
    print('\n')
    print("-"*10)
      # create and save new credential.
    save_credential(create_credential(u_name, m_password, p_number, e_address))
    print(
        f"New Credentials: username = {u_name} , password = {m_password} created")
    print("-"*16)
    print("Enter command login -to login to your account")
      


if __name__ == '__main__':
  main()
