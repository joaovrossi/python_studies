salário=(float(input("What's your current salary?")))
aumento=(float(input("How much is your salary being increased?")))
porcentagem=salário*aumento/100
salário_final=salário+porcentagem
print(f'If your current salary is {salário} and it will receive a {aumento}% increase,Then you will earn {salário_final}')