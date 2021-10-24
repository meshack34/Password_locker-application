import unittest
import pyperclip
from user import User


class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating user test cases
  '''

  def setUp(self):
    ''' run before each test cases in User'''
    self.createnew_user = User("meshack", "kimutai","meshkim", "0718908494", "meshackkimutai34@gmail.com")  

  def tearDown(self):
    '''clean up after each test case has run. '''
    User.user_list = []

  def test_init(self):
    '''  test if the object is initialized properly'''

    self.assertEqual(self.createnew_user.first_name, "meshack")
    self.assertEqual(self.createnew_user.last_name, "kimutai")
    self.assertEqual(self.createnew_user.user_name, "meshkim")
    self.assertEqual(self.createnew_user.phone_number, "0718908494")
    self.assertEqual(self.createnew_user.email, "meshackkimutai34@gmail.com")
  def test_save_user(self):
    '''test case to test if the user object is saved in list''' 
    self.createnew_user.newuser_save()  # saving the user
    self.assertEqual(len(User.user_list), 0)


if __name__ == '__main__':
    unittest.main()
