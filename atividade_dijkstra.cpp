#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <chrono> // Para medir o tempo de execucao (Teste Grande)
#include <cstdlib> // Para gerar numeros aleatorios

using namespace std;

typedef pair<int, int> Par;
const int INF = numeric_limits<int>::max();

// Funcao Principal do Dijkstra
void dijkstra(int V, const vector<vector<Par>>& grafo, int origem, bool imprimirDetalhos = true) {
    auto inicio = chrono::high_resolution_clock::now();

    vector<int> dist(V, INF);
    vector<int> pred(V, -1);
    
    priority_queue<Par, vector<Par>, greater<Par>> pq;

    dist[origem] = 0;
    pq.push({0, origem});

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (d > dist[u]) continue;

        for (auto aresta : grafo[u]) {
            int v = aresta.first;
            int peso = aresta.second;

            if (dist[u] + peso < dist[v]) {
                dist[v] = dist[u] + peso;
                pred[v] = u;
                pq.push({dist[v], v});
            }
        }
    }

    auto fim = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> tempoMs = fim - inicio;

    // Se o teste for muito grande, nao imprimimos a tabela gigante na tela
    if (imprimirDetalhos) {
        cout << "Vertice\tDistancia\tPredecessor" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << "\t";
            if (dist[i] == INF) cout << "INF\t\t-";
            else cout << dist[i] << "\t\t" << pred[i];
            cout << endl;
        }
    }
    cout << "Tempo de Execucao: " << tempoMs.count() << " ms" << endl << endl;
}

// -------------------------------------------------------------
// TESTE 1: Pequena Instancia (5 vertices)
// -------------------------------------------------------------
void rodarTeste1_Pequeno() {
    cout << "=== TESTE 1: PEQUENA INSTANCIA (5 Vertices) ===" << endl;
    int V = 5;
    vector<vector<Par>> grafo(V);

    grafo[0].push_back({1, 10});
    grafo[0].push_back({2, 3});
    grafo[1].push_back({2, 1});
    grafo[1].push_back({3, 2});
    grafo[2].push_back({1, 4});
    grafo[2].push_back({3, 8});
    grafo[2].push_back({4, 2});
    grafo[3].push_back({4, 7});

    dijkstra(V, grafo, 0, true); // imprime a tabela completa
}

// -------------------------------------------------------------
// TESTE 2: Media Instancia (15 vertices)
// -------------------------------------------------------------
void rodarTeste2_Medio() {
    cout << "=== TESTE 2: MEDIA INSTANCIA (15 Vertices) ===" << endl;
    int V = 15;
    vector<vector<Par>> grafo(V);

    // Conectando os vertices em cadeia e com atalhos
    for (int i = 0; i < V - 1; i++) {
        grafo[i].push_back({i + 1, (i % 5) + 1}); // aresta i -> i+1
        if (i + 2 < V) {
            grafo[i].push_back({i + 2, (i % 3) + 2}); // atalho i -> i+2
        }
    }

    dijkstra(V, grafo, 0, true); // imprime a tabela completa
}

// -------------------------------------------------------------
// TESTE 3: Grande Instancia (2.000 vertices e muitas arestas)
// -------------------------------------------------------------
void rodarTeste3_Grande() {
    cout << "=== TESTE 3: GRANDE INSTANCIA (2.000 Vertices) ===" << endl;
    int V = 2000;
    vector<vector<Par>> grafo(V);

    // Gerando arestas aleatorias para simular um grafo denso
    srand(42); // semente fixa para reprodutibilidade
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < 10; j++) { // cada vertice aponta para ~10 vizinhos
            int destino = rand() % V;
            int peso = (rand() % 100) + 1; // pesos de 1 a 100
            if (i != destino) {
                grafo[i].push_back({destino, peso});
            }
        }
    }

    // Passamos 'false' para nao poluir o terminal com 2.000 linhas de print
    dijkstra(V, grafo, 0, false); 
}

int main() {
    rodarTeste1_Pequeno();
    rodarTeste2_Medio();
    rodarTeste3_Grande();

    return 0;
}