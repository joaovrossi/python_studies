import random
first=(str(input('write the first name:')))
second=(str(input('write the second name:')))
third=(str(input('write the third name:')))
fourth=(str(input('write the fourth name:')))
print(f'The chosen was{random.sample([first, second, third, fourth] , k=1)}')