# Name:Lynn Mumia
# Section: 5
# homework_3.py
import math
import csv

##### Template for Homework 3, exercises 5.1 - 5.5 ######

# **********  Exercise 5.1 ********** 

# Bugs
##### BUG 1 #####
#There is no bug in the first code.
#res is not defined and hence will throw an error.

##### BUG 2 #####
#The student equated the negated number to the initial number before calling the number on
#the function and so the result would be the same number.
#The variable neg_b is not initially defined

##### BUG 3 #####
#The last function does not return the boolean
#Big is not defined.
#The function is not called/invoked hence no results presented out


# **********  Exercise 5.2 ********** 

# Define "Mutable" and list what data structures have this characteristic
#Mutable data structures can be editted after created 
#**Lists
#**Dictionaries
#**Strings

# Define "Immutable" and list what data structures have this characteristic
#They cannot be modified after they have been created. Elements of the data structures
#cannot be modified
#**Tuples




# **********  Exercise 5.3 **********

def ball_collide(ball1, ball2):
    '''
    Computes whether or not two balls are colliding
    
    ball1: a tuple of (x-coord, y-coord, radius) nums (ints or floats);
        represents first ball
    ball2: a tuple of (x-coord, y-coord, radius) nums (ints or floats); 
        represents second ball

    returns: True if the balls collide and False if they do not collide
    '''
    ##### YOUR CODE HERE #####
    dx=(ball2[0]-ball1[0])
    dy=(ball2[1]-ball1[1])
    radius_sum=ball1[2] + ball2[2]
    distance= math.sqrt(math.pow(dx,2)+ math.pow(dy,2))
    if(distance<=radius_sum):
        return True
    else:
        return False



# Test Cases for Exercise 5.3
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True


# **********  Exercise 5.4 **********
class_dict={
    "CS101" :"Intermediate computer programming",
    "CS102" :"Database Management",
    "CS103": "Data Mining",
    "BA101" : "Leadership iv",
    "BA102": "Research Methods"
    }    
    

def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary
    
    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    ##### YOUR CODE HERE #####
    class_dict.update({class_num:desc})
    

def print_classes(course, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken
    
    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''
    ##### YOUR CODE HERE #####
    cs="CS101"
    ba= "BA101"
    if cs in course:
        print class_dict[cs]
    elif ba in course:
        print class_dict[ba]
    else:
        print "No course "+ course + " classes taken"
    

# Test Cases for Exercise 5.4
##### YOUR CODE HERE #####
add_class("CS101", "Software engineering",class_dict)
print class_dict.values()

print_classes("CS101",class_dict)
print_classes("CS",class_dict)
# **********  Exercise 5.5 **********

def buildAddrBook(fileName):
    '''
    Builds an address book from a file.
    
    fileName: a string, the name of the file to read in
     File must be in the format specified in Exercise 5.5.

    returns: a dictionary with keys(firstname,lastname) and values(list with
    phonenumber and email)generated
      from the file, as specified in Exercise 5.5.
    '''
    ## Your Code Here #    
    with open(fileName) as f:
        lines = {}
        for line in f:
            splitted_line = line.split(',')
            splitted_line[-1] = splitted_line[-1].split('\n')[0]
            name = splitted_line[0] + ', ' + splitted_line[1]
            length_of_line = len(splitted_line)
            contact_info = []
            for i in range(2,length_of_line):
                contact_info.append(splitted_line[i])
            lines.update({name :contact_info})
        return lines
        

def changeEntry(addrBook, entry, field, newValue):
    
    '''
    Changes one entry in the specified address book.

    addrBook: a dictionary in the address book format
      returned by buildAddrBook.
    entry: a string; the pre-existing entry to change
    field: a string; the field to change (one of: "name",
      "phoneNumber", "emailAddress")
    newValue: the new value for the specified field

    returns: nothing; only modifies addrBook
    '''
    ## Your Code Here ##
    try:
        temp_dict_value = addrBook[entry];
        if field == 'name':
            del addrBook[entry]
            addrBook.update({newValue: temp_dict_value})
            return
        elif field == 'phoneNumber':
            del addrBook[entry]
            temp_dict_value[0] = newValue;
            addrBook.update({entry: temp_dict_value})
            return
        elif field == 'emailAddress':
            del addrBook[entry]
            temp_dict_value.append(newValue);
            addrBook.update({entry: temp_dict_value})
            return
        else:
            return 'Unexpected field: %s' %(field)
        
    except KeyError as error:
        return 'Invalid entry: %s'%(str(entry))
    
      
addrBook = buildAddrBook('rawAddresses.csv')
print addrBook
"""
changeEntry(addrBook, 'Lemon, Liz', 'emailAddress', 'lizzing@starwars.net')
print addrBook

changeEntry(addrBook, 'Lemon, Liz', 'phoneNumber', '1-900-OKFACE')
print addrBook

changeEntry(addrBook, 'Lemon, Liz', 'name', 'Lemon, Elizabeth')
print addrBook

changeEntry(addrBook, 'Bitdiddle, Ben', 'emailAddress', 'bitdiddly@bu.edu')
changeEntry(addrBook, 'Manchu, Foo', 'homeAddress', 'Baltimore, MD')

print addrBook['Lemon, Liz']
"""
