import unittest
import main


class TestMain(unittest.TestCase):

    def test_two_inputs(self):

        self.assertEqual(main.permutation_checker(), "jimmy")



if __name__ == '__main__':
    unittest.main()