#Conhecendo a builtins "assert"

#
# assert 2 == 3
#
# assert 5 <= 7

# def soma(x,y):
#     res = x + y
#     return res
#
# try:
#     assert soma(2,2) == 5
# except:
#     assert  AssertionError

class Pessoa():
    nome = ''
    idade = 0

    def get_nome(self):
        return  self.nome

    def get_idade(self):
        return self.idade

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

nova_pessoa = Pessoa()
nova_pessoa.set_nome('Thalyta')

assert isinstance(nova_pessoa, Pessoa)
assert nova_pessoa.get_nome() == 'Thalyta'

