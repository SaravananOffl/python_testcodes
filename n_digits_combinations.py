#We need math to call pow() 
import math

#Function to print n_digits_combination
def n_digits_combinations(n):
    numbers = []
    for i in range(pow(10, n)):
        a = str(i).zfill(n)
        numbers.append(a)
        print(a)

