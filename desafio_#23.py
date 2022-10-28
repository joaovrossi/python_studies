numero=int(input('Choose a number from 0 to 9999'))
u = numero// 1 % 10
d = numero// 10 % 10
c = numero// 100 % 10
m = numero// 1000 % 10
print('Analisando número:')
print(f'Unit{u} \nTens {d} \nHundred {c} \nThousand {m}')