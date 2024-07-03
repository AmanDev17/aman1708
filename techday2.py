#if statement
             #code of block to execute if condition is true
             #less than , greater than , less than equal to, greater than equal to , and , not, equal to , not equal to
age = 18 
if age>=18 :
    print("you are eligible to vote")

# if else statement
                   # if condition :
                   # code of block to execute if condition is true
                   #else condition:
                   # code of block to execute when if condition is false
citizen = "true"
if age>= 18:
   if citizen == "true":
      print ("eligible")
   else:
       print ("not eligilble")
else:
    print("not eligible")

#elif (try & accept & switch){do not use it more}
#if
#block of code executed when condition 1 is true
#elif
#block of code executed when condition 2 is true
#else
#block of code executed when bot the conditions are false

score = 85
if score >= 90:
    print("a") 
elif score>=80:
    print("b")
else:
    print("c")

#logical operators
#and operator - true if both condition or statements are true
#or operator - true if anyone condition or statement is true
#not operator - 

age1=19
citizenship=True
if age1>=16 and citizenship:
    print("eligible")

#ternary operator (condition expresssion)
#syntax 
#variable = print value if true condition else value if false
#type.variable()

age2=77
citizenship
voting_status = "eligible to vote" if age>=18 and citizenship else "not eligible"


#list
#syntax
#abc = {"apple","banana","orange"}

abc = {"apple","banana","orange"}
if "apple" in abc:
    print("apple is in list")

#dictionary
#syntax
#lmn = [key:"value", key:"value"]


#non blocking code
#all the codes are running except one 
#synchronizing and asynchronising
#try and except used to have control of block of code instead of if and else

try:
    age3= int(input("enter age:"))
    if age>=18:
        print("eligible")
    else :
        print("not eligible")
except ValueError:
    print("invalid input please enter a number")

#json
#search api 
#restful api - client updates information on the website from user interface
#designations in data analyst

#simple triangle pattern
# pyramid

n=5 
for i in range (1,n+1):
    print("*"*i)

#inverted triangle
m=5
for i in range(n,0,-1):
    print("*"*i)


#right angled triangle
k=5
for i in range (1,n+1):
    print(" "*(n-1)+"*"*i)
#_ _ _ _*
#_ _ _**
# 

# pyramid pattern
h=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

#inverted pyramid
l=5
for i in range (n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))


# diamond pattern
p=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range (n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))

# number triangle pattern 
o=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#floyd triangle
n=5
num=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num +=1
    print()

# pascals triangle
e=5
for i in range(n):
    print(" "*(n-1),end=" ")
    number =1
    for j in range (i+1):
        print(number,end=" ")
        number = number * (i-j)//(j+1)
    print()

# math package installation**********************************************************

