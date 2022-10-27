# Faça um programa que leia um número inteiro e que mostre na tela seu antecessor e seu sucessor.
base_number=(int(input('Choose a number.')))
calculation_number=(1)
print('The number chosen is {} which is preceded by {} and followed by {}'.format(base_number,base_number-calculation_number, base_number+calculation_number))