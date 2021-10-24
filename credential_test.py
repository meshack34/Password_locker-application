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
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential(
            "James", "Muriuki", "0712345678", "james@ms.com")  # create contact object

  def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name, "James")
        self.assertEqual(self.new_credential.last_name, "Muriuki")
        self.assertEqual(self.new_credential.phone_number, "0712345678")
        self.assertEqual(self.new_credential.email, "james@ms.com")

        
  if __name__ == '__main__':
    unittest.main()
