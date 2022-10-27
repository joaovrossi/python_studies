preço=(float(input('Digite o preço do produto: R$')))
desconto=(float(input('Digite o valor do desconto:')))
desconto_final=preço*desconto/100
preço_final=preço-desconto_final
print(f'Aplicando o desconto de {desconto}% no preço R${preço} o preço se torna R${preço_final}')