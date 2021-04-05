import unittest
import HammingDistance

class TestHamming(unittest.TestCase):

    def test_hamming_distance(self): #test_"nameFunction"
        result = HammingDistance.hamming_distance("adcde","bcdef")
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()