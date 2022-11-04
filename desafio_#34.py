salary = int(input("What's your salary?"))
if salary>1249:
    aum = ((salary*10)/100) + salary
    print(f'Your salary will rise to ${aum}! Congratulations!')
if salary<1249:
    aum = ((salary*15)/100) + salary
    print(f'Your salary will rise to ${aum}! Congratulations!')