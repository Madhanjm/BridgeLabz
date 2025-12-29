import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account=BankAccount("Madhan",10000)
    
    def tearDown(self):
        self.account = None
    
    def test_initial_balance(self):
        self.assertTrue(self.account.get_balance() > 0)
        self.assertFalse(self.account.get_balance() < 0)
        self.assertEqual(self.account.get_balance(),10000)
        
    def test_deposite(self):
        self.assertEqual(self.account.deposite(500),10500)
        
    def test_withdarwal(self):
        self.assertEqual(self.account.withdrawal(500),9500)
        
    def test_instance(self):
        self.assertIsInstance(self.account, BankAccount)
        
    def test_none(self):
        self.assertIsNone(self.account)
        
    def test_withrawal_exception(self):
        with self.assertRaises(ValueError):
            self.account.withdrawal(20000)


 
