
import pyperclip


class User:
  '''
  Class that creates new intances of users
  '''

  user_list = []  # empty list

  def __init__(self, first_name, last_name, user_name, phone_number, email):

    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.phone_number = phone_number
    self.email = email

  def save_user(self):
    ''' save new user '''
    User.user_list.append(self)
