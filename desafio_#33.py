first = (int(input('Define the first number:')))
second = (int(input('Define the second number:')))
third = (int(input('Define the third number:')))
minor = first
major = third
if second<first and second<third:
    minor = second
if third<first and third<second:
    minor = third
if first>third and first>second:
    major = first
if second>third and second>first:
    major = second
print(f'The biggest number is {major} and the smallest number is {minor}')