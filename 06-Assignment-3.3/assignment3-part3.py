# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
# print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score 	Grade 
# >= 0.9 	A 
# >= 0.8 	B 
# >= 0.7 	C 
# >= 0.6 	D 
# < 0.6 	F
# Enter score: 0.95 
# A
# Enter score: perfect 
# Bad score
# Enter score: 10.0 
#Bad score
# Enter score: 0.75 
#C
# Enter score: 0.5 
#F


# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
# print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score 	Grade
# >= 0.9 	A
# >= 0.8 	B
# >= 0.7 	C
# >= 0.6 	D
# < 0.6 	F
# If the user enters a value out of range, print a suitable error message and exit. For the test, 
# enter a score of 0.85.




try: 
	grade = float(raw_input("Enter score: "))
	if grade >= 0.9 and grade <= 1.0:
		print "A"
	elif grade >= 0.8 and grade <= 0.89:
		print "B"
	elif grade >= 0.7 and grade <= 0.79:
		print "C"
	elif grade >= 0.6 and grade <= 0.69:
		print "D"
	elif grade >= 0.0 and grade < 0.6: 
		print "F"
	else:
		print "Bad score"
except: 
	print "Bad score"