velocidade =(int(input ('Enter vehicle speed:')))
if velocidade <= 80:
    print("Congratulations, continue to drive safely!")
else:
    print(f"You have exceeded the speed limit and will therefore be fined ${((velocidade - 80)*7):.2f}")