"""
This program will give you the hundreds, tens, units of the number you give to it
"""
number = int(raw_input('Write a number: '))
print number,"makes", number/100,"hundreds",number/10%10,"tens", number%10,"units"
