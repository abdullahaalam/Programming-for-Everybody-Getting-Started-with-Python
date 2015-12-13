# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the 
# computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the 
# pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a 
# number. Do not worry about error checking the user input unless you want to - you can assume the user types 
# numbers properly.

# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay 
# which takes two parameters ( hours and  rate).
# Enter Hours: 45 
# Enter Rate: 10 
# Pay: 475.0
# 475 = 40 * 10 + 5 * 1


def computepay(hours, rate):
	if hours > 40: 
		extraHours = hours - 40
		calculate = (40 * rate) + (extraHours * (rate * 1.5))
		return calculate
	else: 
		calculate = hours * rate
		return calculate

hours = float(raw_input("Enter Hours: "))
rate = float(raw_input("Enter Rate: "))
print computepay(hours, rate)
