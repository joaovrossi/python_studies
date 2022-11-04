from datetime import date
year = (int(input('What year would you like to analyze?')))
if year == 0:
    year = date.today ().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The year you chose, {year} is a leap year.")
else:
    print(f"The year you chose, {year} is not a leap year")