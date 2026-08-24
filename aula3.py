import time
import random

def bubble_sort(arr):
    n = len(arr)
    # Variável 'trocou' serve como otimização para parar caso já esteja ordenado
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca manual, garantindo que não estamos usando métodos prontos
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                trocou = True
        # Se não houve troca nesta passada, o vetor já está ordenado
        if not trocou:
            break

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def copiar_vetor(arr):
    # Cópia manual do array para que ambos os algoritmos testem a exata mesma base de dados
    novo_arr = []
    for item in arr:
        novo_arr.append(item)
    return novo_arr

def executar_experimento():
    # Escalonamento com os tamanhos de n especificados na atividade
    tamanhos = [1000,5000,10000,50000,100000] 
    
    for n in tamanhos:
        print(f"\n" + "="*40)
        print(f"MÉTRICAS PARA n = {n}")
        print("="*40)
        
        # Coleta, formatação e apresentação dos dados
        vetor_original = []
        for _ in range(n):
            vetor_original.append(random.randint(0, 10500))
            
        # ---------------------------------------------------------
        # BUBBLE SORT
        # ---------------------------------------------------------
        vetor_bubble = copiar_vetor(vetor_original)
        
        # 1. Executar com vetor gerado (Desordenado)
        inicio = time.perf_counter()
        bubble_sort(vetor_bubble)
        fim = time.perf_counter()
        tempo_bubble_desord = fim - inicio
        print(f"TempoAlgoritmo1 (Bubble Sort - Desordenado): {tempo_bubble_desord:.5f} s")
        
        # 2. Executar novamente com o vetor já ordenado da etapa anterior
        inicio = time.perf_counter()
        bubble_sort(vetor_bubble)
        fim = time.perf_counter()
        tempo_bubble_ord = fim - inicio
        print(f"TempoAlgoritmo1 (Bubble Sort - Ordenado):    {tempo_bubble_ord:.5f} s")

        print("-" * 40)

        # ---------------------------------------------------------
        # INSERTION SORT
        # ---------------------------------------------------------
        vetor_insertion = copiar_vetor(vetor_original)
        
        # 3. Executar com vetor gerado (Desordenado)
        inicio = time.perf_counter()
        insertion_sort(vetor_insertion)
        fim = time.perf_counter()
        tempo_insert_desord = fim - inicio
        print(f"TempoAlgoritmo2 (Insertion Sort - Desordenado): {tempo_insert_desord:.5f} s")
        
        # 4. Executar novamente com o vetor já ordenado da etapa anterior
        inicio = time.perf_counter()
        insertion_sort(vetor_insertion)
        fim = time.perf_counter()
        tempo_insert_ord = fim - inicio
        print(f"TempoAlgoritmo2 (Insertion Sort - Ordenado):    {tempo_insert_ord:.5f} s")

# Inicia a coleta
executar_experimento()