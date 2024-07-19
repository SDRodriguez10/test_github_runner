import unittest

class TestPass(unittest.TestCase):
    """Unit test for CI, check pass"""

    def test_print_hello(self) -> None:
        print("Hello Sebastian")

        self.assertTrue(1 == 1)

if __name__ == "__main__":
    unittest.main()