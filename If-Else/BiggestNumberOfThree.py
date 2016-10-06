"""
This program it's similar to the previous one but with three numbers instead of
two. Checking the biggest number is a really good if-else workout so feel free
to train.
"""

number_one = int(raw_input('Write a number: '))
number_two = int(raw_input('Write another number: '))
number_three = int(raw_input('Write another number: '))

if number_one>number_two and number_one>number_three:
    print number_one,"it's the biggest number"
elif number_two>number_one and number_two>number_three:
    print number_two, "it's the biggest number"
elif number_three>number_one and c>number_two:
    print number_three, "it's the biggest number"
else:
    print "The numbers are equal"
