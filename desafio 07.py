#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
first_grade=(int(input('What was their first grade?')))
second_grade=(int(input('What was their second grade?')))

print('Their grades were {} and {} so in average they scored {}. '.format(first_grade,second_grade,(first_grade+second_grade)//2))