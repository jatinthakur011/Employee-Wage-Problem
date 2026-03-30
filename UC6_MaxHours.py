# Calculate Wages till a condition of total working hours or days is reached for a month - Assume 100 hours and 20 days

print("Welcome to Employee wage computation program on master branch")

wage_per_hour=20
max_working_days=20
max_working_hours=100

total_hours=0
total_days=0
total_wage=0

import random
 # cond. if working days cross 20 or working hours cross 100 it stop
while total_days<max_working_days and total_hours<max_working_hours:

    attendance=random.randint(0,2)
    if attendance==1:
        hours=8
    elif attendance==2:
        hours=4
    else:
        hours=0
        # cond. if total hours are exceeding 100 than we can deduct them
        
        if total_hours+hours>max_working_hours:
            hours=max_working_hours-total_hours
    total_days+=1
    total_hours+=hours
    total_wage+=hours*wage_per_hour

    print("Total Days: ", total_days)
    print("Total Hours: ",total_hours)
    print("Total Wage: ", total_wage)
    print("\n")