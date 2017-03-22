#Name: Lynn Mumia
#Hangman question 1

def maxval(some_list):
    currMax = 6
    if all(val < currMax for val in some_list):
        return True
    else:
        return False
def lesssix(some_list):
    for val in some_list:
        if(val<6):
            return True
        else:
            return False
        
some_list=[1,5,3,4]
some_list2=[5,3,7,5]

print maxval(some_list)
print maxval(some_list2)
print maxval(some_list)
print lesssix(some_list2)

#Question 3a
print "This is just a reminder on loops"
for i in "hello":
    print i
for i in ['a',True,123]:
    print i
