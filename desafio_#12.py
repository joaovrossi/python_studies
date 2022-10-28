preço=(float(input("what's the product's price $")))
desconto=(float(input("How much is the discount being given?")))
desconto_final=preço*desconto/100
preço_final=preço-desconto_final
print(f'If we discount {desconto}% of the original price ${preço} the final cost will be ${preço_final}')