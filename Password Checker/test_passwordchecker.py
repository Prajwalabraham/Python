from typing import IO
import unittest 
from unittest.mock import patch, call
from passwordchecker import PasswordCheck
import io

class Testpasswordchecker(unittest.TestCase):
    
    @patch('builtins.print')
    def test_passwordcheck(self, mock_print):
        password = "Iampass"
        PasswordCheck(password)
        mock_print.assert_has_calls([
            call('LOW'),
            call('The rules that contribute least towards your password strength\n'),
            call("Your password doesn't start with a Number"),
            call('Your password has lowercase characters')
            ])

    @patch('builtins.print')
    def test_passwordcheck1(self, mock_print):
        PasswordCheck("Iampassword1")
        mock_print.assert_has_calls([
            call('AVERAGE'),
            call('The rules that contribute least towards your password strength\n'),
            call("Your password doesn't start with a Number"),
            call('Your password has atleast 8 characters')
            ])

    @patch('builtins.print')
    def test_passwordcheck2(self, mock_print):
        PasswordCheck("Iam123@!pass")
        mock_print.assert_has_calls([
            call('VERY GOOD')
            ])

    @patch('builtins.print')
    def test_passwordcheck3(self, mock_print):
        PasswordCheck("1Pass@1")
        mock_print.assert_has_calls([
            call('AVERAGE'),
            call('The rules that contribute least towards your password strength\n'),
            call("Your password has lowercase characters"),
            call('Your password has uppercase characters')
            ])
    
    @patch('builtins.print')
    def test_passwordcheck4(self, mock_print):
        PasswordCheck("1pass@@1")
        mock_print.assert_has_calls([
            call('GOOD')
            ])
    
    @patch('builtins.print')
    def test_passwordcheck5(self, mock_print):
        PasswordCheck("Pa@@!")
        mock_print.assert_has_calls([
            call('AVERAGE'),
            call('The rules that contribute least towards your password strength\n'),
            call("Your password doesn't start with a Number"),
            call('Your password has lowercase characters')
            ])
    @patch('builtins.print')
    def test_passwordcheck6(self, mock_print):
        PasswordCheck("pass")
        mock_print.assert_has_calls([
            call('LOW'),
            call('The rules that contribute least towards your password strength\n'),
            call("Your password doesn't start with a Number"),
            call('Your password has lowercase characters')
            ])

    @patch('builtins.print')
    def test_passwordcheck7(self, mock_print):
        PasswordCheck("12@@!!")
        mock_print.assert_has_calls([
            call('AVERAGE'),
            call('The rules that contribute least towards your password strength\n'),
            call("Your password contains more than 2 special characters"),
            call('Your password contains more than 2 numbers')
            ])
if __name__=="__main__":
    unittest.main()