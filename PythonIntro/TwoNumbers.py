"""
This will be a good starting point in python as it is a simple program
number_one and number_two are variables so we declare it before equal sign
the value of number_one as an example is int(raw_input('Write a number: ')).

Now I will explain it better raw_input('something: ') will print 'something: '
to the console and wait for some user input to store it in number_one.
So, raw_input() prints what we put between parenthesis and waits for user input
and finally returns the input that the user gave us.
But in this particular case we want a number so if the user gives us something
else then a number it will return him an error. That's why we put int() around it.
To transform what is between parenthesis.

So, step by step we ask for a number with the message 'Write a number: ' the user gives us
6 and the console will think that is a word '6' so we write int('6') and finally we
get our 6.

Finally the print keyword prints something to the console.

Hope that exampled helped you and happy coding.
"""
number_one = int(raw_input('Write a number: '))
number_two = int(raw_input('Write another number: '))

print "Sum: ", number_one+number_two, "Product: " ,number_one*number_two,\
      "Subtraction",number_one-number_two, "Division: ",number_one/number_two,\
      "Rest: ", number_one%number_two,"Exponentiation", number_one**number_two
