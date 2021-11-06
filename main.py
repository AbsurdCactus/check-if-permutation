
def permutation_checker(string_one, string_two):

    if len(string_one) != len(string_two):

        print(string_one, string_two, "false")

        return False

    string_one = list(string_one)
    string_two = list(string_two)

    string_one.sort()
    string_two.sort()

    return string_one == string_two
