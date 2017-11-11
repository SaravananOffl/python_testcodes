#Function to print all four digits numbers
def FourDigCom():
    numbers=[]
    for i in range(10000):
        a=str(i).zfill(4)
        print(a)
        numbers.append(a)

    
