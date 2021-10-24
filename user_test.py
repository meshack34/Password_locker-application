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
    User.myuserlist = []

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
    self.assertEqual(len(User.myuserlist), 1)

  def test_add_multiple_user(self):
    '''for multible user  '''
    self.createnew_user.newuser_save()
    test_user = User("meshu", "kimu", "meshkim","0748872955", "meshackkimutai34@gmail.com")  # new user
    test_user.newuser_save()
    self.assertEqual(len(User.myuserlist), 2)

  def test_delete_user(self):
    ''' delete a user from the list '''
    self.createnew_user.newuser_save()
    test_user = User("meshu", "kimu", "meshkim", "0748872955","meshackkimutai34@gmail.com")  # new user
    test_user.newuser_save()
    self.createnew_user.delete_myuser()  # Deleting a user object
    self.assertEqual(len(User.myuserlist), 1)

  def test_find_user_by_number(self):
    '''
    test to check if we can find a user by phone number and display information
    '''

    self.createnew_user.newuser_save()
    test_user = User("meshu", "kimu", "meshkim", "0748872955",
                   "meshackkimutai34@gmail.com")
    test_user.newuser_save()

    found_user = User.find_by_phoneNumber("0748872955")

    self.assertEqual(found_user.email, test_user.email)

  def test_user_exists(self):
        test_user = User("meshu", "kimu", "meshkim", "0748872955",
                   "meshackkimutai34@gmail.com")

        test_user.newuser_save()
        user_exists = User.user_exist("0748872955")
    
        self.assertTrue(user_exists)

  def test_display_all_users(self):
    '''
    method that returns a list of all users saved
    '''
    self.assertEqual(User.display_users(), User.user_list)

  def test_copy_email(self):
      '''
        Test to confirm that we are copying the email address from a found user
        '''

      self.createnew_user.newuser_save()
      User.copy_email("0718908494")

      self.assertEqual(self.new_user.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
