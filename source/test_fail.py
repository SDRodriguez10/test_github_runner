import unittest
import numpy as np

class TestPass(unittest.TestCase):
    """Unit test for CI, check fail"""

    def test_num_diff(self) -> None:
        """Test 2 uint8's are different"""
        arr_1 = np.array([0, 1]*10, dtype=np.uint8)
        arr_2 = np.array([1, 1]*10, dtype=np.uint8)

        self.assertTrue((arr_1 != arr_2).all)

if __name__ == "__main__":
    unittest.main()