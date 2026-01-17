class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, 
    carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# Criando os objetos
moto = Motocicleta("preta", "abc-1234", 2)
print(f"Motocicleta - Cor: {moto.cor}, Placa: {moto.placa}, Rodas: {moto.numero_rodas}")
moto.ligar_motor()

carro = Carro("branco", "cab-4321", 4)
print(f"Carro - Cor: {carro.cor}, Placa: {carro.placa}, Rodas: {carro.numero_rodas}")
carro.ligar_motor()

caminhao = Caminhao("Verde", "vou-0420", 8, False)
print(f"Caminhão - Cor: {caminhao.cor}, Placa: {caminhao.placa}, Rodas: {caminhao.numero_rodas}")
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)


print(moto)
print(carro)
print(caminhao)
