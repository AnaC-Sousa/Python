"""
This program reads three numbers from user input and prints to the screen
the number of even numbers and the number of odd numbers
"""
number_one = int(raw_input('Write a number: '))
number_two = int(raw_input('Write another number: '))
number_three = int(raw_input('Write another number: '))

even = 0
odd = 0

#We will test the three numbers
#First one
if number_one%2==0:
    even+=number_one #this adds number one to even. The same as even=even+number_one
else:
    odd+=number_one

#Second    
if number_two%2==0:
    even+=number_two
else:
    odd+=number_two

#Third
if number_three%2==0:
    even+=number_three
else:
    odd+=number_three

print "There are", even, "Even number and", odd, "odd numbers"
