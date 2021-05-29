from Main import User
import unittest
from Main import Credentials
import pyperclip

class test_user_input(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        """
        This method provides test inputs to test
        """
        self.user = User("rotichenoch27@gmail.com", "1234", "1234")
        
    def test_init(self):
        """
        This method check for correct initialization
        """
        self.assertEqual(self.user.email, "rotichenoch27@gmail.com")
        self.assertEqual(self.user.password, "1234")
        self.assertEqual(self.user.confirmPassword, "1234")
        
    def tearDown(self):
        '''
        This is a method to clear list after every test
        '''
        User.users = []

    def test_multiple_users(self):
        self.user = User("enochrotich27@gmail.com", "1234", "1234")
        self.user.saveUser()
        self.assertEqual(len(User.users), 1)
        
    def test_createUser(self):
        self.user = User("enochrotich27@gmail.com", "1234", "1234") #New user
        self.assertEqual(self.user.email, "enochrotich27@gmail.com")


if __name__ == '__main__':
    unittest.main()
