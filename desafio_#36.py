velocidade =(int(input ('Enter vehicle speed:')))
if velocidade <= 80:
    print("\033[0;32mCongratulations, continue to drive safely!")
else:
    print(f"\033[0;33m'You have exceeded the speed limit and will therefore be fined \033[0;31m${((velocidade - 80)*7):.2f}")