# create an array with 10.000 int values (randomized). order the array and verify which values are prime numbers
import random
import time

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
    primes = []
    for i in range(len(arr)):
        if is_prime(arr[i]):
            primes.append(arr[i])
    return primes

inicio = time.perf_counter()
fim = time.perf_counter()

# build the array with n random values (0 to 15.000)
n = 10000
numbers = [0] * n

for i in range(n):
    numbers[i] = random.randint(0, 15000)
    
# sort the array
sorted_array = merge_sort(numbers)

# verify if the array is ordered
for i in range(20):
    print(sorted_array[i])

tempo_total = (fim - inicio) * 100000
print(f"Tempo: {tempo_total:.2f} ms")
  