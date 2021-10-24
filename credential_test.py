import pyperclip
import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
  '''
  Test class that defines test cases for the credential class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating credential test cases
  '''

  def setUp(self):
    '''
    Set up method to run before each test cases in credential
    '''
    self.new_credential = Credential(
        "meshkim", "1234567890", "0718908494","meshackkimutai34@gmail.com")  # creating credential object

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    Credential.mycredential_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_credential.credential_userName, "meshkim")
    self.assertEqual(self.new_credential.password, "1234567890")
    self.assertEqual(self.new_credential.phonenumber, "0718908494")
    self.assertEqual(self.new_credential.credential_email, "meshackkimutai34@gmail.com")


  def test_save_credential(self):
    ''' test_save_credential test case to test if the credential saved into '''
    self.new_credential.save_credential()  # saving the credential
    self.assertEqual(len(Credential.mycredential_list), 1)

  def test_delete_thecredential(self):
    '''
    To test if we can remove a credential from list
    '''
    self.new_credential.save_credential()
    test_credential = Credential("newmesh", "newpassword", "0748872955","meshackkimutai345@gmail.com")  # add credential
    test_credential.save_credential()
    self.new_credential.delete_credentials()  # remove the credential object
    self.assertEqual(len(Credential.mycredential_list), 1)

  def test_save_multiple_credential(self):
    '''
    test_save_multiple_credential to check if we can save multiple contact
    objects to our contact list
    '''
    self.new_credential.save_credential()
    test_credential = Credential(
        "newmesh", "newpassword", "0748872955", "meshackkimutai345@gmail.com")  # add credential
    test_credential.save_credential()
    self.assertEqual(len(Credential.mycredential_list), 2)

  def test_find_credential_by_number(self):
   ''' check if can find credentials using phone numbers'''
   self.new_credential.save_credential()
   testmy_credentials = Credential(   "newmesh", "newpassword", "0748872955", "meshackkimutai345@gmail.com")  # add credential
   testmy_credentials.save_credential()

   getallmy_credentials = Credential.find_by_phoneNumber("0748872955")

   self.assertEqual(getallmy_credentials.credential_userName, testmy_credentials.credential_userName)

   def test_credential_exists(self):
    '''test if  a credential exist and return a Boolean '''

    self.new_credential.save_credential() 
    test_mycredentials = Credential("newmesh", "newpassword", "0748872955", "meshackkimutai345@gmail.com")  # add credential
    test_mycredentials.save_credential()

    check_mycredentialsexist = Credential.checkcredential_exist("0748872955")
    self.assertTrue(check_mycredentialsexist)

  def test_display_all_credentials(self):
    '''
    method that returns a list of all credentials saved
    '''
    self.assertEqual(Credential.display_credentials(),
                     Credential.mycredential_list)

  def test_copy_email(self):
      '''
        Test to confirm that we are copying the email address from a found credential
        '''

      self.new_credential.save_credential()
      Credential.copy_pwd("0718908494")

      self.assertEqual(self.new_credential.password, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
