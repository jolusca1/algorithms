import random

# Entendendo o funcionamento do quicksort

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
array1 = [random.randint(0, 100000) for _ in range(1000)]
print(quicksort(array1))