import unittest
import Designing_Rugs

class TestHamming(unittest.TestCase):

    def test_make_rug(self): #test_"nameFunction"
        result = Designing_Rugs.make_rug(3,2,'')
        self.assertEqual(result,['','',''])
        # self.assertEqual(result,['AA','AA','AA'])

if __name__ == '__main__':
    unittest.main()