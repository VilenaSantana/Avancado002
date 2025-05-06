class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome=nome
        self.idade=idade
        self.peso=peso
    def comer(self,comida):
        print(f"{self.nome} foi comer {comida}")
    def falar(self):
        print(f"{self.nome} está falando")
    def dormir(self):
        print(f"{self.nome} foi domir")