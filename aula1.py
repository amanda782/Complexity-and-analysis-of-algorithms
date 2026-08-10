# create an array with 10.000 int values (randomized). order the array and verify which values are prime numbers
import random

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

# build the array with 10.000 random values (0 to 15.000)
numbers = [0] * 10000
for i in range(10000):
    numbers[i] = random.randint(0, 15000)

# sort it once so both options can reuse the sorted array
sorted_array = merge_sort(numbers)

# simple menu to choose the feature
while True:
    print("")
    print("==========================")
    print("1 - Show the sorted array")
    print("2 - Show the prime numbers")
    print("0 - Exit")
    print("==========================")
    print("")

    option = input("Choose an option: ")

    if option == "1":
        print("The complete sorted array is:")
        print("")
        print(sorted_array)
    elif option == "2":
        primes = find_primes(sorted_array)
        print("Found", len(primes), "prime numbers on this array:")
        print("")
        print(primes)
    elif option == "0":
        break                        
    else:
        print("Invalid option")



