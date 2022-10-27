salário=(float(input('Qual é o salário atual?R$')))
aumento=(float(input('Quanto % ele irá aumentar?')))
porcentagem=salário*aumento/100
salário_final=salário+porcentagem
print(f'Se seu salário é de {salário} e receberá um aumento de {aumento}%, então você receberá R${salário_final}')