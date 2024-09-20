import unittest
from shoppingCart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.item = ShoppingCart()

    def test_add_item(self):
        self.item.add_item('apple', 2, 10)
        self.assertEqual(len(self.item.items), 1)
        self.assertEqual(self.item.items[0], {'name': 'apple', 'price': 2, 'quantity': 10})

        self.item.add_item('banana', 3, 5)
        self.assertEqual(len(self.item.items), 2)
        self.assertEqual(self.item.items[1], {'name': 'banana', 'price': 3, 'quantity': 5})

    def test_add_zero_quantity_items(self):
        with self.assertRaises(ValueError) as error:
            self.item.add_item('apple', 2, 0)
        self.assertEqual(str(error.exception), "Quantity must be greater than 0")

    def test_add_negative_quantity(self):
        with self.assertRaises(ValueError) as error:
            self.item.add_item('apple', 2, -1)
        self.assertEqual(str(error.exception), "Quantity must be greater than 0")

    def test_total_price(self):
        self.item.add_item('apple', 2, 10)
        self.item.add_item('banana', 3, 5)
        self.assertEqual(self.item.total_price(), 35)

    def test_remove_item(self):
        self.item.add_item('apple', 2, 10)
        self.item.add_item('banana', 3, 5)
        self.item.remove_item('apple')
        self.assertEqual(len(self.item.items), 1)
        self.assertEqual(self.item.items[0]['name'], 'banana')

    def test_item_is_empty(self):
        self.assertTrue(self.item.is_empty())
        self.item.add_item('apple', 2, 10)
        self.item.add_item('banana', 3, 5)
        self.assertFalse(self.item.is_empty())


if __name__ == '__main__':
    unittest.main()