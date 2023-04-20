line1= (float(input("Define the first line's size:")))
line2= (float(input("Define the second line's size:")))
line3= (float(input("Define the third line's size:")))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('These lines can form a triangle!')
else:
    print("These lines can't form a triangle!")