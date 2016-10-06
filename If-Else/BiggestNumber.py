"""
This program gives with the greatest number of the two given by the user input
"""
number_one = int(raw_input('Write a number: '))
number_two = int(raw_input('Write another number: '))

if number_one > number_two:
    print number_one, "e' maior que ", number_two
elif number_two > number_one: #This is a new sentence to you, it evaluates another if condition
                              #inside the test of that if
    print number_two," e' maior que ", number_one
else:
    print number_one," e ",number_two," sao iguais"
