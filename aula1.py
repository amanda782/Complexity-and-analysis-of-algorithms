# create an array with 10.000 int values (randomized). order the array and verify which values are prime numbers
import random
import time

def mergeFinal(arr):
    inicioMerge = time.perf_counter()
    result = merge_sort(arr)
    fimMerge = time.perf_counter()
    tempo_total_merge = (fimMerge - inicioMerge) * 1000
    print(f"Tempo merge: {tempo_total_merge:.2f} ms")
    return result


# ordering with merge sort
def merge_sort(arr):
    if(len(arr) <=1):
        return arr

    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return(merge(left, right))

# receives two sorted arrays and returns a single sorted array
def merge(left, right):
    result = [0] * (len(left) + len(right))
    k=0
    i = 0
    j=0

    while i < len(left) and j < len(right):
        if(left[i] <= right[j]):
            result[k] = left[i]
            i+=1
            k+=1
        else:
            result[k] = right[j]
            j+=1
            k+=1
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1

    return result

# verify if its prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
    
# try to find primes on the array
def find_primes(arr):
    inicioPrimos = time.perf_counter()
    primes = []
    for i in range(len(arr)):
        if is_prime(arr[i]):
            primes.append(arr[i])
    fimPrimos = time.perf_counter()
    tempo_total_primos = (fimPrimos - inicioPrimos) * 1000
    print(f"Tempo primos: {tempo_total_primos:.2f} ms")
    print(f"O número de primos encontrados foi: {len(primes)}")
    return primes

# build the array with n random values (0 to 15.000)
def gerar(n):
    inicioArray = time.perf_counter()
    numbers = [0] * n
    for i in range(n):
        numbers[i] = random.randint(0, 15000)
    fimArray = time.perf_counter()
    tempo_total_gerar = (fimArray - inicioArray) * 1000
    print(f"Tempo gerar: {tempo_total_gerar:.2f} ms")
    return numbers


inicioTotal = time.perf_counter()
n = 1000
# generate ONE array and keep the original (unordered) reference
array_desordenado = gerar(n)
# sort the SAME array
sorted_array = mergeFinal(array_desordenado)
sorted_again_array = mergeFinal(sorted_array)

# verify if the array is ordered
for i in range(20):
    print(sorted_array[i])


primosDesordenados = find_primes(array_desordenado)
primosOrdenados = find_primes(sorted_array)
fimTotal = time.perf_counter()
tempo_total_geral = (fimTotal - inicioTotal) * 1000
print(f"Tempo geral: {tempo_total_geral:.2f} ms")

  