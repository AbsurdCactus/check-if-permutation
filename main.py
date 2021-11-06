from unittest.main import main



def permutation_checker(string_one, string_two):
    
    string_two = [string_two]
    string_one = [string_one]
    string_one.sort()
    string_two.sort()
    
    if len(string_one) != len(string_two):

        return False

    return string_one == string_two
    
    

        
                
    
  
    
        
    





if __name__ == '__main__':
    main()