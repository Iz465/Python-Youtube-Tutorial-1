course = 'Python for Beginners'
print(len(course)) #len tells us the length of the string
course.upper() # these are called methods. methods are stuff that follow after the .
course.lower # All lower case
course.find('P') # This will print the index of the first p character. it will return 0 as p is the first letter
# the find method is case sensitive. if i typed in p which is lower case it wouldnt work as there is no lowercase p

print(course.find('Beginners')) # this will give 11 as the first letter of Beginngers starts at index 11
print(course.upper())
print(course.replace('Beginners', 'Absolute Beginners')) # This method replaces Beginners with Absolute Beginners
print ('Python' in course) # This expression is a boolen it will print True or False depending on whether correct or not