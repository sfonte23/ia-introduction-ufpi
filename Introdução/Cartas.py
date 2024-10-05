'''Um ambiente é considerado parcialmente observável quando o agente não consegue perceber completamente o estado do ambiente. '''

import random

class JogoDeCartas:
    def __init__(self):
        self.cartas_jogador = ['A', '2', '3', '4']
        self.cartas_oponente = ['5', '6', '7', '8']  # O jogador não pode ver estas cartas
    
    def mostrar_cartas_jogador(self):
        print(f"Cartas do jogador: {', '.join(self.cartas_jogador)}")
    
    def carta_oponente(self):
        # O agente pode apenas escolher aleatoriamente uma carta do oponente para adivinhar
        return random.choice(self.cartas_oponente)

class AgenteCartas:
    def __init__(self, jogo):
        self.jogo = jogo

    def jogar(self):
        # O agente tenta adivinhar uma carta do oponente
        carta_adivinhada = self.jogo.carta_oponente()
        print(f"O agente adivinhou que a carta do oponente é: {carta_adivinhada}")

# Simulação do ambiente parcialmente observável
jogo = JogoDeCartas()
agente = AgenteCartas(jogo)

print("Estado do jogo:")
jogo.mostrar_cartas_jogador()

agente.jogar()
