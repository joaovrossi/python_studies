velocidade =(int(input ('Insira a velocidade do veiculo:')))
if velocidade <= 80:
    print("Parabéns, continue a dirigir com segurança!")
else:
    print(f"Você ultrapassou o limite de velocidade e portanto será multado em R${((velocidade - 80)*7):.2f}")