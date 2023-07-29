class AnagramChecker:
    """ This is a class that check if an object/string is an anagram """

    def __init__(self, s1, s2):
        """ Constructor - Define instance/object variable here"""
        self.s1 = s1
        self.s2 = s2


    def AnagramCheck(self):
        """ Class Method - A function that checks if two strings are anagram of each other """
        string_1 = self.s1.replace(" ", "").lower()
        string_2 = self.s2.replace(" ", "").lower()

        if sorted(string_1) == sorted(string_2):
            print(f"{string_1} is an anagram of {string_2}")
        else:
            print(f"{string_1} is not an anagram of {string_2}")


# Object
words = AnagramChecker("silent", "listen")
words.AnagramCheck()