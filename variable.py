#string data type
name="aman"
print(type(name))
'''here aman is a string hence we use double quots whereas in boolean and
 null data type we will not use any double quots'''
#integer data type
roll_number=411
print(type(roll_number))
#float data type
percentage=83.60
print(type(percentage))
#boolean data type
is_student=True
print(type(is_student))
#null data type
have_doneAnyJob=None
print(type(have_doneAnyJob))
'''we can print all the data separately 
or else as shown below'''
#print(name,roll_number,percentage,is_student,have_doneAnyJob)
'''we can update the data 
and print again to see changes '''
percentage=88.90
print(name,roll_number,percentage,is_student,have_doneAnyJob)


print("My name is " + name + " and my roll number is",roll_number)
      #here we cannot 
      #concatenate that is we cannot add two different types of data types
       #in one print statement hence we use commas instead of +___+ operators'''
print("I have scored",percentage)
print("in class 10th and I am a student is a ",is_student ,"statement")