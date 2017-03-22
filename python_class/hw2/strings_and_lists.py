# Name:
# Section:
# strings_and_lists.py

# **********  Exercise 4.1 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])

def cumulative_sum(number_list):
    # number_list is a list of numbers

    ##### YOUR CODE HERE #####
    first= number_list[0]
    second= first + number_list[1]
    third= second + number_list[2]    
    return (first,second,third)


# Test Cases
##### YOUR CODE HERE #####
number_list=[4,3,6]
print cumulative_sum(number_list)
# **********  Exercise 4.2 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin

    ##### YOUR CODE HERE #####
   suffix="ay"
   wanted=word[1:len(word)]
   new_word= wanted + suffix
   return new_word
    

# Test Cases
##### YOUR CODE HERE #####
print pig_latin("mum")

# **********  HW 2 complete! *********
