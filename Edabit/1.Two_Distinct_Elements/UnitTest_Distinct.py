import unittest
import Distinct_Elements

class TestCalc(unittest.TestCase):

    def test_return_unique(self):
        lst = '1','9','8','8','7','6','1','6'
        result = Distinct_Elements.return_unique(lst)
        self.assertEqual(result,['9','7'])

if __name__ == '__main__':
    unittest.main()