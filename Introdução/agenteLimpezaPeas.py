''' Este exemplo ilustra como um agente pode operar em um ambiente, utilizando as quatro componentes do modelo PEAS. O agente toma decisões com base em suas percepções do ambiente e age para cumprir seu objetivo (limpar a sujeira). '''

import random

class Ambiente:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = [[random.choice([0, 1]) for _ in range(tamanho)] for _ in range(tamanho)]
        self.agent_pos = (0, 0)  # Posição inicial do agente

    def mostrar(self):
        for i in range(self.tamanho):
            print(" ".join(str(x) for x in self.matriz[i]))
        print("Agente na posição:", self.agent_pos)

    def esta_sujo(self, pos):
        x, y = pos
        return self.matriz[x][y] == 1

    def limpar(self, pos):
        x, y = pos
        print(f"Limpando a posição {pos}.")
        self.matriz[x][y] = 0  # Limpa a área

    def mover(self, nova_pos):
        if 0 <= nova_pos[0] < self.tamanho and 0 <= nova_pos[1] < self.tamanho:
            self.agent_pos = nova_pos
        else:
            print("Movimento inválido!")

class AgenteLimpeza:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.areas_limpas = 0  # Contador de áreas limpas
        self.iteracoes = 0     # Contador de iterações

    def executar(self):
        x, y = self.ambiente.agent_pos
        self.iteracoes += 1  # Incrementa o contador de iterações

        if self.ambiente.esta_sujo((x, y)):
            self.ambiente.limpar((x, y))
            self.areas_limpas += 1  # Incrementa o contador de áreas limpas
        else:
            print(f"A posição {self.ambiente.agent_pos} já está limpa.")

        movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
        movimento = random.choice(movimentos)
        nova_pos = (x + movimento[0], y + movimento[1])
        self.ambiente.mover(nova_pos)

    def mostrar_performance(self):
        print(f"Número de áreas limpas: {self.areas_limpas}")
        print(f"Número de iterações: {self.iteracoes}")

# Simulação
tamanho_do_ambiente = 5
ambiente = Ambiente(tamanho_do_ambiente)
agente = AgenteLimpeza(ambiente)

# Executar o agente algumas vezes para simular o comportamento
for _ in range(10):
    ambiente.mostrar()
    agente.executar()
    print("-----")

# Mostrar a performance final do agente
agente.mostrar_performance()


