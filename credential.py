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

  @classmethod
  def find_by_phoneNumber(cls, phonenumber):
    ''' take a phonenumber and return matching credentials '''
    for credential in cls.mycredential_list:
      if credential.phonenumber == phonenumber:
        return credential
@classmethod
def checkcredential_exist(cls, phonenumber):
    ''' checks if a credential exist and return boolean '''
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
