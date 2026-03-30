# UC4 - Switch Case Statement

print("Welcome to Employee wage computation program on master branch")

wages_per_hour=20
full_time=8
half_time=4

import random
attendance=random.randint(0,2)

match attendance:
    case 1:
        hours=8
    case 2:
        hours=4
    case _:
        hours=0

daily_wages=hours*wages_per_hour
print("working hours: ",hours)
print("daily wages: ",daily_wages)