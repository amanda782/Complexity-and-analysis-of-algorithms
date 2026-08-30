import time
import random
import sys

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        
        # Cópia manual para o vetor da Esquerda (L)
        L = []
        for i in range(mid):
            L.append(arr[i])
            
        # Cópia manual para o vetor da Direita (R)
        R = []
        for i in range(mid, n):
            R.append(arr[i])

        # Chamadas recursivas
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        
        # Intercalando os vetores temporários de volta no vetor original
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Verificando se sobrou algum elemento na Esquerda
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Verificando se sobrou algum elemento na Direita
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(arr, low, high):
    # Escolhe o pivô no meio para evitar lentidão extrema em vetores já ordenados
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid] 
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def copiar_vetor(arr):
    novo_arr = []
    for item in arr:
        novo_arr.append(item)
    return novo_arr

def executar_experimento():
    # Tamanhos exigidos para a Aula 4
    tamanhos = [1000, 5000, 10000, 50000, 100000, 250000, 500000,600000,700000,800000,900000,1000000]
    
    for n in tamanhos:
        print(f"\n" + "="*50)
        print(f"MÉTRICAS PARA n = {n}")
        print("="*50)
        
        # Gerando vetor aleatório (valores de 0 a 10.500)
        vetor_original = []
        for _ in range(n):
            vetor_original.append(random.randint(0, 10500))
            
        vetor_teste = copiar_vetor(vetor_original)
        inicio = time.perf_counter()
        shell_sort(vetor_teste)
        tempo_shell_desord = time.perf_counter() - inicio
        print(f"TempoAlgoritmoShellSort (Desordenado): {tempo_shell_desord:.5f} s")
        
        inicio = time.perf_counter()
        shell_sort(vetor_teste)
        tempo_shell_ord = time.perf_counter() - inicio
        print(f"TempoAlgoritmoShellSort (Ordenado):    {tempo_shell_ord:.5f} s")
        print("-" * 50)

        vetor_teste = copiar_vetor(vetor_original)
        inicio = time.perf_counter()
        quick_sort(vetor_teste, 0, len(vetor_teste) - 1)
        tempo_quick_desord = time.perf_counter() - inicio
        print(f"TempoAlgoritmoQuickSort (Desordenado): {tempo_quick_desord:.5f} s")
        
        inicio = time.perf_counter()
        quick_sort(vetor_teste, 0, len(vetor_teste) - 1)
        tempo_quick_ord = time.perf_counter() - inicio
        print(f"TempoAlgoritmoQuickSort (Ordenado):    {tempo_quick_ord:.5f} s")
        print("-" * 50)

        vetor_teste = copiar_vetor(vetor_original)
        inicio = time.perf_counter()
        merge_sort(vetor_teste)
        tempo_merge_desord = time.perf_counter() - inicio
        print(f"TempoAlgoritmoMergeSort (Desordenado): {tempo_merge_desord:.5f} s")
        
        inicio = time.perf_counter()
        merge_sort(vetor_teste)
        tempo_merge_ord = time.perf_counter() - inicio
        print(f"TempoAlgoritmoMergeSort (Ordenado):    {tempo_merge_ord:.5f} s")

# Inicia o programa
executar_experimento()