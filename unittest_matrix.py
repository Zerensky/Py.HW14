import unittest

from Python_next_deep.Seminar_11 import Matrix

NEW_MATRIX_SQR = Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]])
NEW_MATRIX_SQR_MUL_TEN_ANS = Matrix([[10, 20, 30], [30, 20, 10], [40, 50, 60]])
NEW_MATRIX_RCT = Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]])
NEW_MATRIX_MUL_L = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
NEW_MATRIX_MUL_R = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
MATRIX_MUL_ANS = Matrix([[1, 8, 21, 40], [10, 30, 56, 88], [27, 60, 99, 144]])
MATRIX_RCT_SUM_ANS = Matrix([[2, 4, 6, 8], [8, 10, 12, 14], [16, 18, 20, 22]])


class TestMatrixClass(unittest.TestCase):

    def test_create_success(self):
        assert (NEW_MATRIX_SQR == Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]]))

    def test_eq_success(self):
        self.assertTrue(NEW_MATRIX_SQR == Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]]))
        self.assertFalse(NEW_MATRIX_SQR == Matrix([[1, 2, 3], [3, 2, 4], [4, 5, 6]]))

    def test_ne_success(self):
        self.assertFalse(NEW_MATRIX_SQR != Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]]))
        self.assertTrue(NEW_MATRIX_SQR != Matrix([[1, 2, 3], [3, 2, 4], [4, 5, 6]]))

    def test_matrix_mul_success(self):
        self.assertTrue(NEW_MATRIX_MUL_L * NEW_MATRIX_MUL_R == MATRIX_MUL_ANS)


if __name__ == '__main__':
    unittest.main(verbosity=2)