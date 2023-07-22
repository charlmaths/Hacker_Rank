""" Level 1 """

string_1 = "Silent"
string_2 = "ListeN"

string_1 = string_1.replace(" ", "") # Removes spaces
string_1 = string_1.lower() # Converts to lower case

string_2 = string_2.replace(" ", "") # Removes spaces
string_2 = string_2.lower() # Converts to lower case

string_1_sorted = sorted(string_1)
string_2_sorted = sorted(string_2)

if string_1_sorted == string_2_sorted:
   print(f"{string_1} is an anagram of {string_2}")
else:
   print(f"{string_1} is not an anagram of {string_2}")


""" Level 2 """


def anagram_func(string_1, string_2):
    string_1 = string_1.replace(" ", "").lower()
    string_2 = string_2.replace(" ", "").lower()

    if sorted(string_1) == sorted(string_2):
        print(f"{string_1} is an anagram of {string_2}")
    else:
        print(f"{string_1} is not an anagram of {string_2}")


anagram_func("silent", "lisTeN")


