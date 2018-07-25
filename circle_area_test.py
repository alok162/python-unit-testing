
import unittest
import circle_area


class First_Test(unittest.TestCase):
    def test_area_circle_for_10radius(self):
        result = circle_area.circleArea(10)
        expected = 314.1592653589793
        self.assertEqual(expected, result)

    def test_area_circle_for_20radius(self):
        result = circle_area.circleArea(20)
        expected = 1256.6370614359173
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
