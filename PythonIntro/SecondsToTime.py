"""
This program will give us the time equivalent to the seconds of the user input
"""

seconds = int(raw_input('Seconds please: '))

new_hours = seconds/3600
seconds = seconds - new_hours*3600
new_minutes = seconds/60
seconds = seconds - new_minutes*60

print "sao", new_hours, "horas", new_minutes,"minutos e ",\
          seconds," segundos"
