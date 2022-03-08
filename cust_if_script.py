#!/usr/bin/env python3
"""Alta3 Class - Python Basics | Eric Tedford
   Write custom script utilizing if, elif, and else."""


# Program that prompts for numeric score, then returns grade

message = 'Your letter grade is: '

my_score = float(input("What was your score on your test?"))

if my_score >= 90:
    message = message + "A"
elif my_score >= 80:
    message = message + "B"
elif my_score >= 70:
    message = message + "C"
elif my_score >=60:
    message = message + "D"
else:
    message = message + "F"

print(message)

