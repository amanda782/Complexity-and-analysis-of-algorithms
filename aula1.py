# create an array with 10.000 int values (randomized). order the array and verify wich values are prime numbers
import random

# ordering with merge sort
def merge_sort(arr):
    if(len(arr) <=1):
        return arr
    
    meio = len(arr)//2
    left = arr[:meio]
    right = arr[meio:]

    left = merge_sort(left)
    right = merge_sort(right)

    return(merge(left, right))

#recebe dois arrays ordenados e retorna um array ordenado
def merge(esq, dir):
    result = [0] * (len(esq) + len(dir))   
    k=0
    i = 0
    j=0

    while i < len(esq) and j < len(dir):
        if(esq[i] <= dir[j]):
            result[k] = esq[i]
            i+=1
            k+=1
        else:
            result[k] = dir[j]
            j+=1
            k+=1
    while i < len(esq):                                                                                                   
        result[k] = esq[i]                                                                                             
        i += 1                                                                                                            
        k += 1                                                                                                            
                                                                                                                        
    while j < len(dir):                                                                                                   
        result[k] = dir[j]                                                                                             
        j += 1                                                                                                            
        k += 1  

    return result   

def its_prime(arr):
    for i in len(arr):
        if(arr[i] <=2):
            
numbers = [0] * 10000

for i in range(10000):
    numbers[i] = random.randint(0, 15000)

call = merge_sort(numbers);

for x in range(20):
    print(call[x])


    
# verify if its prime

