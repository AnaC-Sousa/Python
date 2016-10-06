"""
This program will calculate the amount of money you have when you tell it
how many five cents, two cents and one cent coins you have.
"""

five_cents = int(raw_input('how many five cents coins? '))
two_cents = int(raw_input('how many two cents coins? '))
one_cent = int(raw_input('how many one cent coins? '))
print "The amount of money you have is", 5*five_cents+2*two_cents+one_cent , "cents"
