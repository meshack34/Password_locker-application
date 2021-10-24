
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

  @classmethod
  def find_by_phoneNumber(cls, phone_number):
    ''' take a phonenumber and return matching credentials '''
    for credential in cls.myuserlist:
      if credential.phone_number == phone_number:
        return credential

  @classmethod
  def checkcredential_exist(cls, phonenumber):
    '''check if it exist and return boolean
    '''
    for credential in cls.mycredential_list:
      if credential.phonenumber == phonenumber:
        return True

    return False

  @classmethod
  def display_credentials(cls):
    '''
    method that returns the credential list
    '''
    return cls.mycredential_list

  @classmethod
  def copy_pwd(cls, phonenumber):
    credential_found = Credential.find_by_phoneNumber(phonenumber)
    pyperclip.copy(credential_found.password)
