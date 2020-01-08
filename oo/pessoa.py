class Pessoa:
    def __init__(self, nome = None, idade = 18):#esse init vai ser sempre executado quando você criar um objeto
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Salve {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Tiago', 18)
    print(p.nome)
    print(p.idade)
    p.nome = 'Biel'
    print(p.nome)
    p.idade = 9
    print(p.idade)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
