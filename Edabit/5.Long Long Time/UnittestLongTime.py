import unittest
import LongTime

class TestLongTime(unittest.TestCase):

    def test_longest_time(self): #test_"nameFunction"
        result = LongTime.longest_time(1,59,3598)
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()

