import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        for quote in quotes:
            stock_name = quote['stock']
            bid_price = quote['top_bid']['price']
            ask_price = quote['top_ask']['price']
            result = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(result, (stock_name, bid_price, ask_price, expected_price))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        for quote in quotes:
            stock_name = quote['stock']
            bid_price = quote['top_bid']['price']
            ask_price = quote['top_ask']['price']
            result = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(result, (stock_name, bid_price, ask_price, expected_price))

    def test_getRatio(self):
        self.assertAlmostEqual(getRatio(100, 50), 2)
        self.assertAlmostEqual(getRatio(100, 25), 4)

    def test_getRatio_zero_division(self):
        with self.assertRaises(ValueError):
            getRatio(100, 0)

if __name__ == '__main__':
    unittest.main()

