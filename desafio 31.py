distância = (int(input('A quantos km está o seu destino?')))
if distância <=200:
    print(f"O preço da sua passagem será de R${distância*0.5:.2f}")
else:
    print(f"O preço da sua passagem será de R${distância*0.45:.2f}")