import unittest
import pyperclip
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
    test_credential = Credential(
        "newmesh", "newpassword", "0748872955","meshackkimutai345@gmail.com")  # new credential
    test_credential.save_credential()
    self.new_credential.delete_credentials()  # remove a credential object
    self.assertEqual(len(Credential.mycredential_list), 1)


if __name__ == '__main__':
    unittest.main()
