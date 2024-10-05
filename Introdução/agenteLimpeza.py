'''Esse é um exemplo didático de um aspirador de pó simulado, onde o agente do aspirador tem sensores para detectar sujeira e atuadores para se mover e limpar. O ambiente será uma casa simples com duas salas: esquerda e direita. O aspirador pode perceber sujeira e sua localização e, com base nessas percepções, ele decide se limpa a sala ou se move para a outra.'''

class Ambiente:
    def __init__(self):
        # O ambiente tem duas salas: Esquerda e Direita
        # 0 = Limpa, 1 = Suja
        self.salas = [1, 1]  # Ambas começam sujas

    def esta_sujo(self, posicao):
        return self.salas[posicao] == 1

    def limpar(self, posicao):
        print(f"Limpando sala {posicao}.")
        self.salas[posicao] = 0

class Aspirador:
    def __init__(self):
        # O aspirador começa na sala 0 (esquerda)
        self.posicao = 0

    def mover_direita(self):
        if self.posicao == 0:
            self.posicao = 1
            print("Movendo para a sala 1 (direita).")

    def mover_esquerda(self):
        if self.posicao == 1:
            self.posicao = 0
            print("Movendo para a sala 0 (esquerda).")

    def executar(self, ambiente):
        # Percebe o ambiente e age de acordo
        if ambiente.esta_sujo(self.posicao):
            ambiente.limpar(self.posicao)
        else:
            print(f"Sala {self.posicao} já está limpa.")

        # Move para outra sala após agir
        if self.posicao == 0:
            self.mover_direita()
        else:
            self.mover_esquerda()

# Simulação
ambiente = Ambiente()
aspirador = Aspirador()

# Executar o aspirador algumas vezes para simular o comportamento
for _ in range(4):
    aspirador.executar(ambiente)
