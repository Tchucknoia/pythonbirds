class Pessoa:
    olhos = 2 #atributo de classe, algo em comum para todos os objetos da classe Pessoas devem ser declarados assim
    def __init__(self, *filhos, nome = None, idade = 18):#esse init vai ser sempre executado quando você criar um objeto
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Salve {id(self)}'


if __name__ == '__main__':
    tiago = Pessoa(nome='Tiago')
    andre = Pessoa(tiago, nome='André', idade=40)
    print(andre.nome)
    print(andre.idade)
    print(andre.filhos)#retorna feio pq oq ta dentro da lista filhos é um objeto feito na linha 12
    for filho in andre.filhos:#pra poder mostrar os nomes dos filhos (sendo todos objetos) faz isso
        print(filho.nome)
    print(tiago.__dict__)#__dict__ é um atributo que retorna todos os outros atributos de instancia em forma de dicionário
    tiago.sobrenome = 'Lachman'#atributo dinâmico se adiciona assim e ele SÓ VALE para aquele objeto
    print(tiago.sobrenome)
    del tiago.idade#o contrario de adicionar o atributo dinamico é remover atributos dinamicamente
    print(tiago.__dict__)
    print(Pessoa.olhos)
    print(tiago.olhos)
    print(andre.olhos)
    andre.olhos = 1
    print(andre.__dict__)
    print(tiago.__dict__)
    print(Pessoa.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(tiago.olhos)
    print(andre.olhos)
    print(andre.__dict__)
    print(tiago.__dict__)
    print(Pessoa.__dict__)
    Pessoa.olhos = 4
    del andre.olhos
    print(Pessoa.olhos)
    print(tiago.olhos)
    print(andre.olhos)
    print(andre.__dict__)
    print(tiago.__dict__)
    print(Pessoa.__dict__)
