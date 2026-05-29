year="2026"
lis_cal=[]

months_days=[("01",31),("02",28),("03",31),("04",30),("05",31),("06",30),("07",31),("08",31),("09",30),("10",31),("11",30),("12",31)]

for mnth_str,mnth_days in month_days:
    for day in range(1,mnth_days+1):
        if day>=10:
            day_str=str(day)
        else:
            day_str="0"+str(day)
            
        lis_cal.append(day_str+ mnth_str+ year)

print(lis_cal)
