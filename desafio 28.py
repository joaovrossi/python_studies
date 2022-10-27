import random
num = random.randrange(0,5)
guess = input('Try to guess what number was chosen from 0 to 5')
if guess==num:
    print('Congratulations, you chose the right number!')
else:
    print(f"I'm sorry, you picked the wrong number. It was actually {num}")