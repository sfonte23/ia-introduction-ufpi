'''Um ambiente é considerado completamente observável se o agente pode perceber todo o estado do ambiente a qualquer momento. Um exemplo disso é um tabuleiro de xadrez, onde todas as peças são visíveis.'''

class TabuleiroXadrez:
    def __init__(self):
        # Inicializando um tabuleiro de xadrez com peças representadas por números
        self.tabuleiro = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ]
    
    def mostrar(self):
        for linha in self.tabuleiro:
            print(" ".join(linha))
        print()

class AgenteXadrez:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def escolher_movimento(self):
        # Exemplo simples: o agente escolhe mover o primeiro peão que encontra
        for i, linha in enumerate(self.tabuleiro.tabuleiro):
            for j, peça in enumerate(linha):
                if peça == 'P':  # Peão branco
                    print(f"Mover peão de ({i}, {j}) para ({i+1}, {j})")
                    self.tabuleiro.tabuleiro[i][j] = '.'  # Remove o peão do lugar atual
                    self.tabuleiro.tabuleiro[i+1][j] = 'P'  # Move o peão para a nova posição
                    return

# Simulação do ambiente completamente observável
tabuleiro = TabuleiroXadrez()
agente = AgenteXadrez(tabuleiro)

print("Tabuleiro inicial:")
tabuleiro.mostrar()

agente.escolher_movimento()

print("Tabuleiro após o movimento:")
tabuleiro.mostrar()
