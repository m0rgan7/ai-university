# Análise do Problema da Mochila

---

## 1. O que significa ser um algoritmo estocástico?

- Algoritmos estocásticos utilizam elementos de **aleatoriedade** durante a execução.  
- Isso faz com que, para a mesma entrada, possam gerar resultados diferentes em execuções distintas.  
- Diferente de algoritmos **determinísticos**, que sempre produzem o mesmo resultado para a mesma entrada.  
- No nosso código, exemplos de aleatoriedade são: geração inicial de soluções, mutações, escolha de vizinhos e aceitação probabilística de soluções.

---

## 2. O Hill Climbing travou em soluções locais?

- Sim, o Hill Climbing clássico **costuma travar em ótimos locais**.  
- Isso porque ele só aceita movimentos para soluções melhores, sem explorar piores soluções temporariamente.  
- Assim, pode parar em um ótimo local e não alcançar o ótimo global.

---

## 3. O Simulated Annealing conseguiu escapar de ótimos locais?

- Sim, o Simulated Annealing permite aceitar soluções piores com certa probabilidade, que diminui ao longo do tempo (temperatura).  
- Isso permite que ele **escape de mínimos locais** e explore o espaço de soluções de forma mais ampla.  
- Geralmente, encontra soluções melhores e mais próximas do ótimo global que o Hill Climbing.

---

## 4. O Algoritmo Genético trouxe diversidade e soluções mais próximas do ótimo?

- Sim, o Algoritmo Genético mantém uma população de soluções e utiliza **crossover** e **mutação** para explorar diferentes regiões do espaço de busca.  
- Essa diversidade genética ajuda a evitar convergência prematura e aumenta as chances de encontrar soluções próximas do ótimo global.  
- A seleção baseada no fitness promove a evolução contínua das soluções.

---

## 5. Qual método foi mais rápido? E qual foi mais eficaz?

- **Mais rápido:** geralmente, o Hill Climbing, pois explora apenas vizinhos locais e não realiza operações complexas.  
- **Mais eficaz:** Simulated Annealing e Algoritmo Genético tendem a obter melhores soluções em problemas com muitos ótimos locais, graças aos seus mecanismos para escapar desses pontos.

---

## 6. Coleta e análise dos resultados

Foram coletados os resultados de 300 execuções para cada algoritmo e calculadas as seguintes métricas:

- **Valor médio encontrado**  
- **Melhor valor obtido**  
- **Número de soluções diferentes encontradas**  
- **Solução(ões) mais frequente(s)** e sua frequência  
- **Desvio padrão** para medir consistência

---

## 7. Comparação dos algoritmos

| Algoritmo           | Valor Médio | Melhor Valor | Soluções Únicas | Mais Frequente | Frequência | Desvio Padrão |
|---------------------|-------------|--------------|-----------------|----------------|------------|---------------|
| Hill Climbing       |  XYZ        | XYZ          | XYZ             | XYZ            | XYZ        | XYZ           |
| Simulated Annealing |  XYZ        | XYZ          | XYZ             | XYZ            | XYZ        | XYZ           |
| Algoritmo Genético  |  XYZ        | XYZ          | XYZ             | XYZ            | XYZ        | XYZ           |

---

## 8. Considerações finais

- **Hill Climbing:** rápido, mas pode ficar preso em ótimos locais.  
- **Simulated Annealing:** mais lento, porém capaz de escapar de mínimos locais e encontrar soluções melhores.  
- **Algoritmo Genético:** explora uma população diversificada, balanceando exploração e explotação, frequentemente chegando perto do ótimo global.

---

Quer ajuda para incluir a análise automática desses resultados no seu projeto?  
Posso te ajudar a criar o código que gera essas métricas e imprime esse relatório automaticamente.
