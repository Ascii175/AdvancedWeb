import unittest
import Characters_ASCII

class Testdict(unittest.TestCase):

    def test_to_dict(self): #test_"nameFunction"       
        lst = 'a','b','c'
        result = Characters_ASCII.to_dict(lst)
        self.assertEqual(result,[{'a': 97}, {'b': 98}, {'c': 99}])

if __name__ == '__main__':
    unittest.main()