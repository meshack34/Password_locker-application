
import pyperclip


class User:
  ''' new intances of users '''

  myuserlist = []  # empty list

  def __init__(self, first_name, last_name, user_name, phone_number, email):

    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.phone_number = phone_number
    self.email = email

  def newuser_save(self):
    ''' save new user '''
    User.myuserlist.append(self)

  def delete_myuser(self):
    '''deletes a saved user from the list '''

    User.myuserlist.remove(self)
