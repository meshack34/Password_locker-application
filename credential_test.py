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
        "meshackkimutai", "1234567890", "0718908494")  # creating credential object


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_credential.credential_name,"meshackkimutai")
    self.assertEqual(self.new_credential.password,"1234567890")
    self.assertEqual(self.new_credential.number,"0718908494")


if __name__ == '__main__':
    unittest.main()
