#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <chrono> // Para medir o tempo de execucao (Teste Grande)
#include <cstdlib> // Para gerar numeros aleatorios

using namespace std;

typedef pair<int, int> Par;
const long long INF = numeric_limits<long long>::max() / 4;

// Funcao Principal do Dijkstra
void dijkstra(int V, const vector<vector<Par>>& grafo, int origem, bool imprimirDetalhos = true) {

    auto inicio = chrono::high_resolution_clock::now();

    vector<long long> dist(V, INF);
    vector<int> pred(V, -1);

    priority_queue<
        pair<long long, int>,
        vector<pair<long long, int>>,
        greater<pair<long long, int>>
    > pq;

    dist[origem] = 0;
    pq.push({0, origem});

    while (!pq.empty()) {
        long long d = pq.top().first;
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

//Programação Dinâmica
void programacaoDinamica(int V, const vector<vector<Par>>& grafo,
                         int origem, bool imprimirDetalhes = true) {

    auto inicio = chrono::high_resolution_clock::now();

    // Cada linha representa uma etapa e cada coluna um vertice.
    // dp[k][v] = menor custo para chegar a v usando ate k arestas.
    vector<vector<long long>> dp(V, vector<long long>(V, INF));

    // Caso base: distancia da origem ate ela mesma.
    dp[0][origem] = 0;

    // Preenchimento da tabela por etapas.
    for (int k = 1; k < V; k++) {

        // Mantem os resultados da etapa anterior.
        dp[k] = dp[k - 1];

        // Percorre todos os vertices.
        for (int u = 0; u < V; u++) {

            // Ignora vertices que ainda nao foram alcancados.
            if (dp[k - 1][u] == INF) continue;

            // Percorre as arestas que saem do vertice u.
            for (auto aresta : grafo[u]) {
                int v = aresta.first;
                int peso = aresta.second;

                long long novoCusto = dp[k - 1][u] + peso;

                // Atualiza se encontrar um caminho mais barato.
                if (novoCusto < dp[k][v]) {
                    dp[k][v] = novoCusto;
                }
            }
        }
    }

    // Verificacao de ciclos negativos alcancaveis pela origem.
    bool cicloNegativo = false;

    for (int u = 0; u < V; u++) {
        if (dp[V - 1][u] == INF) continue;

        for (auto aresta : grafo[u]) {
            int v = aresta.first;
            int peso = aresta.second;

            if (dp[V - 1][u] + peso < dp[V - 1][v]) {
                cicloNegativo = true;
                break;
            }
        }

        if (cicloNegativo) break;
    }

    auto fim = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> tempoMs = fim - inicio;

    // Exibe os resultados da ultima etapa.
    if (imprimirDetalhes) {
        cout << "Vertice\tDistancia Minima" << endl;

        for (int i = 0; i < V; i++) {
            cout << i << "\t";

            if (dp[V - 1][i] == INF) {
                cout << "INF";
            } else {
                cout << dp[V - 1][i];
            }

            cout << endl;
        }
    }

    if (cicloNegativo) {
        cout << "ATENCAO: Foi detectado um ciclo negativo "
             << "alcancavel a partir da origem." << endl;
        cout << "As distancias dos vertices afetados podem "
             << "nao possuir um valor minimo finito." << endl;
    } else {
        cout << "Nenhum ciclo negativo alcancavel foi detectado."
             << endl;
    }

    cout << "Tempo de Execucao: " << tempoMs.count()
         << " ms" << endl << endl;
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

    cout << "\n--- DIJKSTRA ---" << endl;
    dijkstra(V, grafo, 0, true);

    cout << "--- PROGRAMACAO DINAMICA ---" << endl;
    programacaoDinamica(V, grafo, 0, true);
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

    cout << "\n--- DIJKSTRA ---" << endl;
    dijkstra(V, grafo, 0, true);

    cout << "--- PROGRAMACAO DINAMICA ---" << endl;
    programacaoDinamica(V, grafo, 0, true);
}

// -------------------------------------------------------------
// TESTE 3: Grande Instancia (2.000 vertices e muitas arestas)
// -------------------------------------------------------------
void rodarTeste3_Grande() {
    cout << "=== TESTE 3: GRANDE INSTANCIA (2.000 Vertices) ===" << endl;
    int V = 2000;
    vector<vector<Par>> grafo(V);

    // Gerando um grafo aleatorio com aproximadamente 10 arestas por vertice
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
    cout << "\n--- DIJKSTRA ---" << endl;
    dijkstra(V, grafo, 0, false);

    cout << "--- PROGRAMACAO DINAMICA ---" << endl;
    programacaoDinamica(V, grafo, 0, false);
}

// -------------------------------------------------------------
// TESTE 4: Grafo com pesos negativos
// -------------------------------------------------------------
void rodarTeste4_PesosNegativos() {
    cout << "=== TESTE 4: PESOS NEGATIVOS ===" << endl;

    int V = 5;
    vector<vector<Par>> grafo(V);

    grafo[0].push_back({1, 6});
    grafo[0].push_back({2, 7});
    grafo[1].push_back({2, 8});
    grafo[1].push_back({3, 5});
    grafo[1].push_back({4, -4});
    grafo[2].push_back({3, -3});
    grafo[2].push_back({4, 9});
    grafo[3].push_back({1, -2});
    grafo[3].push_back({4, 7});

    cout << "\n--- DIJKSTRA ---" << endl;
    dijkstra(V, grafo, 0, true);

    cout << "--- PROGRAMACAO DINAMICA ---" << endl;
    programacaoDinamica(V, grafo, 0, true);
}

int main() {
    rodarTeste1_Pequeno();
    rodarTeste2_Medio();
    rodarTeste3_Grande();
    rodarTeste4_PesosNegativos();

    return 0;
}