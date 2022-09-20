import unittest

from login_system import*

class Login_System_Test(unittest.TestCase):

    global users
    users = {'ldk44':'rvsoccer', 'ljw91':'saltyfish', 'rvc99':'ancientalien'}

    def test_check_username_password(self):
        users1 = {'ldk44': 'rvsoccer25', 'ljw91': 'saltyfish', 'rvc99': 'ancientalien'}
        check1 = check_username_password(users, 'ldk44', 'rvsoccer')
        check2 = check_username_password(users1, 'ldk44', 'rvsoccer')
        self.assertTrue(check1)
        self.assertFalse(check2)

    def test_is_valid_password(self):
        password = 'Rvsoccer25'
        password2 = 'rvsoccer25'
        password3 = 'RVSOCCER25'
        password4 = 'Rvsoccer'
        check1 = is_valid_password(password)
        check2 = is_valid_password(password2)
        check3 = is_valid_password(password3)
        check4 = is_valid_password(password4)
        self.assertTrue(check1)
        self.assertFalse(check2)
        self.assertFalse(check3)
        self.assertFalse(check4)

    def test_sign_up(self):
        flag = sign_up(users, True, 'ldk44', 'rvsoccer')
        flag2 = sign_up(users, True, 'ldk24', 'rvsoccer')
        self.assertEqual(flag,1)
        self.assertNotEqual(flag,2)



if __name__  == '__main__':
    unittest.main()