distância = (int(input('How many kilometers is your destination?')))
if distância <=200:
    print(f"The price of your ticket will be ${distância*0.5:.2f}")
else:
    print(f"The price of your ticket will be ${distância*0.45:.2f}")