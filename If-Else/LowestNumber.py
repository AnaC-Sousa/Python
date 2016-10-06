"""
Interactive number that gives you the lowest number of the four that you introduce
"""
message = "The lowest number until now is"

number_one=int(raw_input('Write a number: '))
lowest = number_one
print message, lowest

number_two=int(raw_input('Write another number: '))
if number_two < lowest:
    lowest = number_two
print message,lowest

number_three=int(raw_input('Write another number: '))
if number_three < lowest:
    lowest=number_three
print message, lowest

number_four=int(raw_input('Write another number: '))
if number_four < lowest:
    lowest = number_four
print "The final lowest number is", lowest
