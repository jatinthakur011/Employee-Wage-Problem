# UC3 - Part Time Employee Wage

print("Welcome to Employee wage computation program on master branch")

wage_per_hour=20
full_time=1
half_time=2

import random
attendance=random.randint(0,2)

if attendance==full_time:
    hours=8
elif attendance==half_time:
    hours=4
else:
    hours=0

daily_wage=hours*wage_per_hour
print("working hours: ",hours)
print("daily wage: ",daily_wage)