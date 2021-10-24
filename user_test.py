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
    '''
    Set up method to run before each test cases in User
    '''
    self.createnew_user = User("meshack", "kimutai","meshkim", "0718908494",
                         "meshackkimutai34@gmail.com")  # creating user object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name, "Nicholas")
    self.assertEqual(self.new_user.last_name, "Ngetich")
    self.assertEqual(self.new_user.phone_number, "0725470732")
    self.assertEqual(self.new_user.email, "ngetichnicholas903@gmail.com")

  def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
    the user list
    '''
    self.new_user.save_user()  # saving the user
    self.assertEqual(len(User.user_list), 1)



