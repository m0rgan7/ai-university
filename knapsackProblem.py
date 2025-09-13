import random
import numpy as np

itens = [
    {"id": 1,  "valor": 60,  "peso": 10},
    {"id": 2,  "valor": 100, "peso": 20},
    {"id": 3,  "valor": 120, "peso": 30},
    {"id": 4,  "valor": 90,  "peso": 15},
    {"id": 5,  "valor": 30,  "peso": 5},
    {"id": 6,  "valor": 70,  "peso": 12},
    {"id": 7,  "valor": 40,  "peso": 7},
    {"id": 8,  "valor": 160, "peso": 25},
    {"id": 9,  "valor": 20,  "peso": 3},
    {"id": 10, "valor": 50,  "peso": 9},
    {"id": 11, "valor": 110, "peso": 18},
    {"id": 12, "valor": 85,  "peso": 14},
    {"id": 13, "valor": 95,  "peso": 16},
    {"id": 14, "valor": 200, "peso": 28},
    {"id": 15, "valor": 55,  "peso": 6},
]

CAPACIDADE_MAX = 50

def fitness(solucao):
    valor_total = 0
    peso_total = 0
    for i, selecionado in enumerate(solucao):
        if selecionado:
            valor_total += itens[i]["valor"]
            peso_total += itens[i]["peso"]
    if peso_total > CAPACIDADE_MAX:
        return 0
    return valor_total

def peso_total(solucao):
    return sum(itens[i]["peso"] for i in range(len(solucao)) if solucao[i])

def gerar_solucao_aleatoria():
    solucao = [random.randint(0, 1) for _ in range(len(itens))]
    return reparar(solucao)

def reparar(solucao):
    while peso_total(solucao) > CAPACIDADE_MAX:
        idxs = [i for i in range(len(solucao)) if solucao[i]]
        solucao[random.choice(idxs)] = 0
    return solucao

def vizinhos(solucao):
    viz = []
    for i in range(len(solucao)):
        vizinho = solucao[:]
        vizinho[i] = 1 - vizinho[i]
        viz.append(reparar(vizinho))
    return viz

def hill_climbing():
    atual = gerar_solucao_aleatoria()
    melhor_fitness = fitness(atual)
    iteracoes = 0
    while iteracoes < 300:
        melhor_vizinho = atual
        for v in vizinhos(atual):
            if fitness(v) > melhor_fitness:
                melhor_vizinho = v
                melhor_fitness = fitness(v)
        if melhor_vizinho == atual:
            break
        atual = melhor_vizinho
        iteracoes += 1
    return atual, fitness(atual), peso_total(atual)

def simulated_annealing():
    T = 50.0
    Tmin = 0.1
    alpha = 0.95
    passos_por_T = 30

    atual = gerar_solucao_aleatoria()
    melhor = atual[:]
    melhor_valor = fitness(atual)

    while T > Tmin:
        for _ in range(passos_por_T):
            vizinho = atual[:]
            idx = random.randint(0, len(vizinho) - 1)
            vizinho[idx] = 1 - vizinho[idx]
            vizinho = reparar(vizinho)

            delta = fitness(vizinho) - fitness(atual)

            if delta > 0 or random.uniform(0, 1) < np.exp(delta / T):
                atual = vizinho
                if fitness(atual) > melhor_valor:
                    melhor = atual[:]
                    melhor_valor = fitness(atual)
        T *= alpha
    return melhor, fitness(melhor), peso_total(melhor)

def crossover(p1, p2):
    ponto = random.randint(1, len(p1) - 1)
    f1 = reparar(p1[:ponto] + p2[ponto:])
    f2 = reparar(p2[:ponto] + p1[ponto:])
    return f1, f2

def mutacao(ind, p_mut=0.02):
    mutado = ind[:]
    for i in range(len(mutado)):
        if random.random() < p_mut:
            mutado[i] = 1 - mutado[i]
    return reparar(mutado)

def torneio(pop, k=3):
    candidatos = random.sample(pop, k)
    return max(candidatos, key=fitness)

def algoritmo_genetico():
    pop_size = 50
    geracoes = 120
    p_cross = 0.9
    p_mut = 0.02
    elite = 2

    populacao = [gerar_solucao_aleatoria() for _ in range(pop_size)]

    for _ in range(geracoes):
        nova_pop = sorted(populacao, key=fitness, reverse=True)[:elite]
        while len(nova_pop) < pop_size:
            p1 = torneio(populacao)
            p2 = torneio(populacao)
            if random.random() < p_cross:
                f1, f2 = crossover(p1, p2)
            else:
                f1, f2 = p1, p2
            nova_pop.append(mutacao(f1, p_mut))
            if len(nova_pop) < pop_size:
                nova_pop.append(mutacao(f2, p_mut))
        populacao = nova_pop

    melhor = max(populacao, key=fitness)
    return melhor, fitness(melhor), peso_total(melhor)

hc, valor_hc, peso_hc = hill_climbing()
sa, valor_sa, peso_sa = simulated_annealing()
ga, valor_ga, peso_ga = algoritmo_genetico()

print("=== Hill Climbing ===")
print("Itens:", [i+1 for i in range(len(hc)) if hc[i]])
print("Valor:", valor_hc, "| Peso:", peso_hc)

print("\n=== Simulated Annealing ===")
print("Itens:", [i+1 for i in range(len(sa)) if sa[i]])
print("Valor:", valor_sa, "| Peso:", peso_sa)

print("\n=== Algoritmo Genético ===")
print("Itens:", [i+1 for i in range(len(ga)) if ga[i]])
print("Valor:", valor_ga, "| Peso:", peso_ga)