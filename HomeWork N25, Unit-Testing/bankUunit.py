import unittest
from bank import BankAccount


class TestBank(unittest.TestCase):
    def setUp(self):
        self.user = BankAccount("Giorgi", 1500)

    def test_deposit(self):
        self.user.deposit(100)
        self.assertEqual(self.user.get_balance(), 1600)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError) as error:
            self.user.deposit(-100)
        self.assertEqual(str(error.exception), "Deposit amount must be positive")

    def test_withdraw(self):
        self.user.withdraw(900)
        self.assertEqual(self.user.get_balance(), 600)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError) as error:
            self.user.withdraw(1600)
        self.assertEqual(str(error.exception), "Insufficient funds")


if __name__ == '__main__':
    unittest.main()
