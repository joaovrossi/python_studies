from math import sqrt
cat_adj=(float(input('Qual é o comprimento do cateto adjacente?')))
cat_opo=(float(input('Qual é o comprimento do cateto oposto?')))
hi=sqrt(cat_adj**2+cat_opo**2)
print(f'A hipotenusa vai medir {hi:.2f}')