# UC2 - Calculate Daily Employee Wage

print("Welcome to Employee wage computation program on master branch")

wage_per_hour=20
full_day_hour=8

import random
attendance=random.randint(0,1)

if attendance ==1 :
    daily_wage=wage_per_hour*full_day_hour
else:
    daily_wage=0

print("Daily Employee wage: ",daily_wage)

