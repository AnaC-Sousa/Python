"""
Simple if-else workout, given a number between 1 and 5 return it's equivalent
Roman numeration.
"""
number = int(raw_input('Write a number between 1 and 5: '))

if number == 1:
    print "I"
elif number == 2:
    print "II"
elif number == 3:
    print "III"
elif number == 4:
    print "IV"
else:
    print "V"
