'''Um táxi autônomo é um excelente exemplo de agente inteligente que precisa lidar com muitos fatores externos, como o tráfego, semáforos, passageiros, entre outros. Vamos fazer uma versão simplificada que mostre como um motorista de táxi autônomo pode lidar com os agentes externos em um ambiente simulado.'''


import random

class Ambiente:
    def __init__(self):
        # Definindo o estado inicial do semáforo e a presença de pedestres
        self.semaforo = "verde"  # Pode ser "verde", "amarelo" ou "vermelho"
        self.pedestre = False  # Se há um pedestre atravessando a rua

    def atualizar(self):
        # Atualizar aleatoriamente o estado do semáforo e pedestres
        self.semaforo = random.choice(["verde", "amarelo", "vermelho"])
        self.pedestre = random.choice([True, False])

    def estado_semaforo(self):
        return self.semaforo

    def ha_pedestre(self):
        return self.pedestre

class TaxiAutonomo:
    def __init__(self):
        self.posicao = "ponto de partida"
        self.tem_passageiro = False

    def pegar_passageiro(self):
        if not self.tem_passageiro:
            print("Passageiro entrou no táxi.")
            self.tem_passageiro = True
        else:
            print("Já há um passageiro no táxi.")

    def deixar_passageiro(self):
        if self.tem_passageiro:
            print("Passageiro chegou ao destino e saiu do táxi.")
            self.tem_passageiro = False
        else:
            print("Não há passageiro no táxi.")

    def mover_para(self, destino):
        print(f"Táxi movendo-se para {destino}.")
        self.posicao = destino

    def parar_no_semaforo(self, ambiente):
        estado = ambiente.estado_semaforo()
        if estado == "vermelho":
            print("Semáforo vermelho. Parando o táxi.")
            return True
        elif estado == "amarelo":
            print("Semáforo amarelo. Reduzindo a velocidade.")
        else:
            print("Semáforo verde. Continuando viagem.")
        return False

    def verificar_pedestres(self, ambiente):
        if ambiente.ha_pedestre():
            print("Pedestre atravessando. Parando o táxi.")
            return True
        return False

    def executar(self, ambiente):
        # Atualiza o ambiente
        ambiente.atualizar()

        # Verifica semáforo e pedestres
        if self.parar_no_semaforo(ambiente) or self.verificar_pedestres(ambiente):
            print("Aguardando condições seguras para continuar.")
        else:
            # Táxi pode se mover
            if not self.tem_passageiro:
                self.pegar_passageiro()
                self.mover_para("destino")
            else:
                self.deixar_passageiro()
                self.mover_para("ponto de partida")


# Simulação
ambiente = Ambiente()
taxi = TaxiAutonomo()

# Executar o táxi algumas vezes para simular o comportamento
for _ in range(5):
    taxi.executar(ambiente)
    print("-----")
