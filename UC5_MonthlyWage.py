# Calculating Wages  for a Month Assume 20 Working Day per Month

print("Welcome to Employee wage computation program on master branch")

wages_per_hour=20
full_time=8
half_time=4
working_days=20
total_wages=0
import random

for i in range(1,working_days+1):
    attendance=random.randint(0,2)

    match attendance:
        case 1:
            hours=8
        case 2:
            hours=4
        case _:
            hours=0
    daily_wages=hours*wages_per_hour
    total_wages+=daily_wages
    print("Total Monthly Wage:", total_wages)