import unittest
import CarTimer

class TestTimer(unittest.TestCase):

    def test_car_timer(self):
        result = CarTimer.car_timer(240)
        self.assertEqual(result,4)

if __name__ == '__main__':
    unittest.main()