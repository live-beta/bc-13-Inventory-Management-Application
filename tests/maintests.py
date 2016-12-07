import unittest

class Truth_Test(unittest.TestCase):
    """testing inventory transactions"""
    def test_createUser(self):
        self.assertEqual(self.createUser(),'user name', 'password','category')
    def test_user_save_to_db(self):
        self.assertEqual(self.savetodb(),True) #check on how to assert boolean value
    def test_retrieve_user(self):
        self.assertEqual(self.retrieveuser(),'user name','category')
    def test_user_login(self):
        self.assertEqual(self.user_login(),False)
    def test_database_connection(self):
        self.assertEqual(self.db_connect(),True)
    def test_add_employee(self):
        self.assertEqual(self.)
