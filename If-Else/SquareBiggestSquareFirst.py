"""
This program checks the biggest number and gives the product of the square of the biggest
by the square of the first.
"""
number_one = int(raw_input('iWrite a number: '))
number_two = int(raw_input('Write another number: '))

if number_one==number_two:
    print "The number are equal"
    if number_one==0:
        print "and both zero"
else:
    if nnumber_one>number_two:
        print "square of the biggest by the square of the first",\
              (number_one**2)*(number_one**2)
    else:
        print "square of the biggest by the square of the first",\
              (number_two**2)*(number_one**2)
