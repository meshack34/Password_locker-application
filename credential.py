import pyperclip

class Credential:
  """
  class for new credentials for credentials
  """
  mycredential_list = []

  def __init__(self, credential_userName, password, phonenumber, credential_email):
    self.credential_userName = credential_userName
    self.password = password
    self.phonenumber = phonenumber
    self.credential_email = credential_email

  def save_credential(self):
    '''save_credential method saves credential object into the mycredential_list
    '''
    Credential.mycredential_list.append(self)

  def delete_credentials(self):
    '''
    remove the saved credential from the list
    '''

    Credential.mycredential_list.remove(self)
