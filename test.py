import unittest
import main


class Testlength(unittest.TestCase):

    def test_a_a(self):
        self.assertEqual(main.permutation_checker(
            string_one="a", string_two="a"), True)

    def test_a_aa(self):
        self.assertEqual(main.permutation_checker(
            string_one="a", string_two="aa"), False)

    def test_aa_aa(self):
        self.assertEqual(main.permutation_checker(
            string_one="aa", string_two="aa"), True)

    def test_a_nothing(self):
        self.assertEqual(main.permutation_checker(
            string_one="a", string_two=""), False)

class TestCharacters(unittest.TestCase):

    def test_a_b(self):
        self.assertEqual(main.permutation_checker(
            string_one="a", string_two="b"), False)    

    def test_ab_ba(self):
        self.assertEqual(main.permutation_checker(
            string_one="ab", string_two="ba"), True)

    def test_abb_abc(self):
        self.assertEqual(main.permutation_checker(
            string_one="abb", string_two="abc"), False)

    def test_abc_abb(self):
        self.assertEqual(main.permutation_checker(
            string_one="abc", string_two="abb"), False)

class TestDuplicates(unittest.TestCase):

    def test_aab_abb(self):
        self.assertEqual(main.permutation_checker(
            string_one="aab", string_two="abb"), False)              


if __name__ == '__main__':
    unittest.main()
