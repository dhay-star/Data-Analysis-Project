import unittest
import numpy as np
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
          'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
          'variance': [[9.555555555555557, 0.6666666666666666, 13.555555555555555],
                       [4.222222222222222, 10.666666666666666, 5.555555555555555], 9.209876543209875],
          'standard deviation': [[3.091206165165235, 0.816496580927726, 3.682712429686489],
                                 [2.0548046676563256, 3.265986323710904, 2.357022603955158], 3.03315017762062],
          'max': [[8, 6, 7], [6, 8, 7], 8],
          'min': [[1, 4, 0], [2, 0, 1], 0],
          'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        for key in expected:
            self.assertAlmostEqual(np.array(actual[key]).all(), np.array(expected[key]).all(), msg=key)
