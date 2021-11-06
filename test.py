import unittest
import main


class TestMain(unittest.TestCase):

    def test_length(self):

        self.assertEqual(main.permutation_checker(string_one="a",string_two="aa"), False)
        self.assertEqual(main.permutation_checker(string_one="aaa",string_two="aaa"), True)
        self.assertEqual(main.permutation_checker(string_one="aaa",string_two="aaa "), False)
        self.assertEqual(main.permutation_checker(string_one="",string_two="aaa"), False)
        self.assertEqual(main.permutation_checker(string_one="a",string_two="a"), True)




        
        
        
    

 



if __name__ == '__main__':
    unittest.main()