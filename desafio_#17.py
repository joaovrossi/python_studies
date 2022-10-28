from math import sqrt
cat_adj=(float(input('What is the length of the adjacent side?')))
cat_opo=(float(input('What is the length of the opposite side?')))
hi=sqrt(cat_adj**2+cat_opo**2)
print(f'The hypotenuse will measure {hi:.2f}')