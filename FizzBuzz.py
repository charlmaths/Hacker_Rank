""" FizzBuzz is where we could be asked to write a programme that prints 1 to 100, for example,
and for multiples of '3' print 'fizz', instead of a number, for multiples of '5', print
'buzz'. If the number is a multiple of 3 and 5 print 'FizzBuzz'

Quick recap, multiple of a number is the product value when we multiply a number by another
number (integer no fractions!) e.g. 2 x 0 = 0, 2 x 1 = 2, 2 x 2 = 4... 0, 2, 4, 6... are all multiples of 2 """

# Using while loop:

i = 0 # Initialise at 0
lst = [] # Start with an empty list

# While loop that will iterate 0 to 100

""" If the i mod 15 is = 0, take the index position of i, then change it to "FizzBuzz",
Apply the same logic if i mod 3 = 0, change the value at index position i to "Fizz",
Again, similar to "Buzz"
"""

while i <= 100:
    lst.append(i) # Simply append the values 0-100 into the empty list
    if i % 15 == 0:
        lst[i] = "FizzBuzz"
    elif i % 3 == 0:
        lst[i] = "Fizz"
    elif i % 5 == 0:
        lst[i] = "Buzz"
    i += 1

print(lst)
