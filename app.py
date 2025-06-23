import streamlit as st

st.title("Busca de Caminhos - Algoritmo A*")

st.markdown ("""
## Explicação Teórica: O que é o Algoritmo A\*?

O ** Algoritmo A\*** é um dos algoritmos mais famosos para busca de caminhos ótimos em um grafo, muito usado em **navegação de mapas**, **inteligência artificial** e **jogos**.

### Como o A* funciona?

O A* utiliza a seguinte fórmula de avaliação:

f(n) = g(n) + h(n)

             
Onde:

- **g(n):** Custo real para chegar ao nó atual `n` partindo da origem.
- **h(n):** Heurística → uma estimativa do custo restante para chegar até o destino.
- **f(n):** Custo total estimado para ir da origem até o destino passando por `n`.

### Vantagens do A*:

- Garante encontrar o caminho mais curto (desde que a heurística seja admissível).
- Explora menos caminhos inúteis do que o algoritmo de Dijkstra puro.

### Importância da Heurística:

Uma **boa heurística** aproxima o custo real restante sem superestimá-lo.

Exemplo comum de heurística: **distância em linha reta entre dois pontos no mapa**.

""")

grafo = {
    'CXJ': {'POA': 98, 'GEL': 306},
    'GEL': {'POA': 254, 'CXJ': 306},
    'PFB': {'GRU': 792},
    'POA': {'CXJ': 98, 'GEL': 254, 'FLN': 450, 'GRU': 863},
    'FLN': {'POA': 450, 'GRU': 513},
    'GRU': {'PFB': 792, 'POA': 863, 'FLN': 513},
}


cidades = list(grafo.keys())

import heapq

def a_star(grafo, inicio, objetivo, heuristica):
    # fila de prioridade: (f(n), g(n), cidade atual, caminho percorrido)
    fila = []
    heapq.heappush(fila, (0 + heuristica[inicio], 0, inicio, [inicio]))

    visitados = set()

    while fila:
        f, g, atual, caminho = heapq.heappop(fila)

        if atual == objetivo:
            return caminho, g  # aqui da o caminho encontrado com custo total

        if atual in visitados:
            continue

        visitados.add(atual)

        for vizinho, custo in grafo.get(atual, {}).items():
            if vizinho not in visitados:
                novo_g = g + custo
                novo_f = novo_g + heuristica.get(vizinho, 0)
                heapq.heappush(fila, (novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')  # aqui é quando nao acha nenhum caminho
