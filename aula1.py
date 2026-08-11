# create an array with 10.000 int values (randomized). order the array and verify which values are prime numbers
import random
import time
import sys
sys.setrecursionlimit(1000000)


def mergeFinal(arr):
    inicioMerge = time.perf_counter()
    result, comparacoes = merge_sort(arr)
    fimMerge = time.perf_counter()
    tempo_total_merge = (fimMerge - inicioMerge) * 1000
    print(f"Tempo merge: {tempo_total_merge:.2f} ms")
    print(f"Comparacoes na ordenacao: {comparacoes}")
    return result


# ordering with merge sort. returns (sorted_array, number_of_comparisons)
def merge_sort(arr):
    if(len(arr) <=1):
        return arr, 0

    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]

    left, comp_left = merge_sort(left)
    right, comp_right = merge_sort(right)
    merged, comp_merge = merge(left, right)
    return merged, comp_left + comp_right + comp_merge

# receives two sorted arrays and returns (single sorted array, comparisons made)
def merge(left, right):
    result = [0] * (len(left) + len(right))
    comparacoes = 0
    k=0
    i = 0
    j=0

    while i < len(left) and j < len(right):
        comparacoes += 1  # count each comparison between two elements
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

    return result, comparacoes

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
n = 50000

# generate ONE array; TempoGerar is SHARED by both scenarios of this size
array_desordenado = gerar(n)

# ----- Cenario [Des]: ordena o vetor DESORDENADO -----
print("--- Cenario [Des] (vetor desordenado) ---")
sorted_array = mergeFinal(array_desordenado)     
find_primes(array_desordenado)                   

# ----- Cenario [Ord]: ordena o vetor JA ORDENADO (mesmo TempoGerar) -----
print("--- Cenario [Ord] (vetor ja ordenado) ---")
mergeFinal(sorted_array)                          
find_primes(sorted_array)                         

# verify if the array is ordered
for i in range(20):
    print(sorted_array[i])

fimTotal = time.perf_counter()
tempo_total_geral = (fimTotal - inicioTotal) * 1000
print(f"Tempo geral: {tempo_total_geral:.2f} ms")

  