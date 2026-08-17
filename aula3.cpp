#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

// Implementação manual do Bubble Sort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        bool trocou = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                trocou = true;
            }
        }
        if (!trocou) break;
    }
}

// Implementação manual do Insertion Sort
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int chave = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > chave) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = chave;
    }
}

// Cópia manual de elementos entre arrays
void copiarVetor(int origem[], int destino[], int n) {
    for (int i = 0; i < n; i++) {
        destino[i] = origem[i];
    }
}

void executarExperimento() {
    // Array com todos os tamanhos solicitados
    int tamanhos[] = {1000, 5000, 10000, 50000, 100000, 500000, 1000000};
    int numTamanhos = 7;
    
    // Inicializa a semente randômica
    srand(time(NULL));

    for (int t = 0; t < numTamanhos; t++) {
        int n = tamanhos[t];
        cout << "\n========================================" << endl;
        cout << "MÉTRICAS PARA n = " << n << endl;
        cout << "========================================" << endl;

        // Alocação manual na Heap para suportar 1.000.000 de inteiros
        int* vetorOriginal = new int[n];
        for (int i = 0; i < n; i++) {
            vetorOriginal[i] = rand() % 10501; // Valores randômicos de 0 a 10500
        }

        int* vetorTeste = new int[n];

        // ---------------------------------------------------------
        // BUBBLE SORT
        // ---------------------------------------------------------
        copiarVetor(vetorOriginal, vetorTeste, n);
        
        clock_t inicio = clock();
        bubbleSort(vetorTeste, n);
        clock_t fim = clock();
        double tempoBubbleDesord = (double)(fim - inicio) / CLOCKS_PER_SEC;
        cout << "TempoAlgoritmo1 (Bubble Sort - Desordenado): " << tempoBubbleDesord << " s" << endl;

        inicio = clock();
        bubbleSort(vetorTeste, n);
        fim = clock();
        double tempoBubbleOrd = (double)(fim - inicio) / CLOCKS_PER_SEC;
        cout << "TempoAlgoritmo1 (Bubble Sort - Ordenado):    " << tempoBubbleOrd << " s" << endl;

        cout << "----------------------------------------" << endl;

        // ---------------------------------------------------------
        // INSERTION SORT
        // ---------------------------------------------------------
        copiarVetor(vetorOriginal, vetorTeste, n);
        
        inicio = clock();
        insertionSort(vetorTeste, n);
        fim = clock();
        double tempoInsertDesord = (double)(fim - inicio) / CLOCKS_PER_SEC;
        cout << "TempoAlgoritmo2 (Insertion Sort - Desordenado): " << tempoInsertDesord << " s" << endl;

        inicio = clock();
        insertionSort(vetorTeste, n);
        fim = clock();
        double tempoInsertOrd = (double)(fim - inicio) / CLOCKS_PER_SEC;
        cout << "TempoAlgoritmo2 (Insertion Sort - Ordenado):    " << tempoInsertOrd << " s" << endl;

        // Liberação rigorosa da memória alocada
        delete[] vetorOriginal;
        delete[] vetorTeste;
    }
}

int main() {
    executarExperimento();
    return 0;
}