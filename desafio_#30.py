num = (int(input("Select a number:")))
numtxt = str(num).strip()
numfinal = numtxt[(len(numtxt)-1):]
if numfinal in ['0','2','4','6','8']:
    print("The number you choose is an even number.")
else:
    print("The number you chose is an odd number.")