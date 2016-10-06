"""
This program will give you the respective seconds of the hours, minutes and seconds
of the user input.
"""
hours = int(raw_input('Hours please: '))
minutes = int(raw_input('Minutes please: '))
seconds = int(raw_input('Seconds please: '))

print hours,"Hour(s)",minutes,"minutes",seconds,"Seconds equals",\
          hours*3600+minutes*60+seconds,"Seconds"
