# Classes e seus metodos
class Hello:
    def  __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # metodos publicos
    def print_variavel_nome_publico(self):
        print(self.nome)

    def _print_variavel_nome_privado(self):
        print(self.none)

Hello("Higor Diego", 20).print_variavel_nome_privado()



