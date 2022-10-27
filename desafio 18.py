import math
angulo=(float(input('Escolha o ângulo:')))
seno= math.sin(math.radians(angulo))
cos= math.cos(math.radians(angulo))
tan= math.tan(math.radians(angulo))
print(f'Seno é {seno:.2f} \nCosceno é {cos:.2f} \nTangente é {tan:.2f}')