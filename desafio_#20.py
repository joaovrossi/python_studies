import random
first=(str(input('Enter the first name:')))
second=(str(input('Enter the second name:')))
third=(str(input('Enter the third name:')))
fourth=(str(input('Enter the fourth name:')))
lista = [first, second, third, fourth]
random.shuffle(lista)
print('The student order will be:')
print(lista)