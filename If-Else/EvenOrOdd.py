"""
In this folder we will introduce you the command if-else.
The if-else sentence will test something then execute it or not.

This works best with an example. We want to test if something is true
or false so we write if 5>4: do something. As 5 is in fact greater than 4
it tests true and will do something. But if it was false it would pass the
sentence.

True and False are of boolean type and are quite useful when you are testing
something.

In this program we will test if the number is even or odd.
"""

number = int(raw_input('Write a number: '))
if number%2==0: #If the number is divisible by 2 it means its even, so it passes
                #the if and prints I'm even to the screen.
    print "I'm even"
else:           #If the number failed the if statment it would execute the else
                #body and would print I'm odd
    print "I'm odd"
