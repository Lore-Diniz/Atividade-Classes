
# 1 - Classe Pessoa

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando objetos
p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)


# 2 - Pessoa com método apresentar

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Olá, meu nome é", self.nome, "e tenho", self.idade, "anos.")

p3 = Pessoa("Carlos", 40)
p3.apresentar()


# 3 - Classe Carro

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

c1 = Carro("Toyota", "Corolla", 2020)
c2 = Carro("Honda", "Civic", 2019)
c3 = Carro("Ford", "Ka", 2018)

print(c1.marca, c1.modelo, c1.ano)
print(c2.marca, c2.modelo, c2.ano)
print(c3.marca, c3.modelo, c3.ano)



# 4 - Alterando atributo

c4 = Carro("Fiat", "Uno", 2015)
print("Antes:", c4.ano)
c4.ano = 2022
print("Depois:", c4.ano)



# 5 - ContaBancaria

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

conta = ContaBancaria("Ana", 100)
conta.depositar(50)
print(conta.saldo)
conta.sacar(120)
print(conta.saldo)


# 6 - ContaBancaria com retorno

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

conta2 = ContaBancaria("Luiz", 200)
if conta2.sacar(100):
    print("Saque ok")
else:
    print("Erro no saque")
print(conta2.saldo)


# =============================
# 7 - Aluno e Turma
# =============================
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return "Aluno: " + self.nome + " - Nota: " + str(self.nota)

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

a1 = Aluno("Mariana", 9.5)
a2 = Aluno("Pedro", 8)
turma = Turma()
turma.adicionar_aluno(a1)
turma.adicionar_aluno(a2)

for aluno in turma.alunos:
    print(aluno)



#  Atributo de classe

class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

dog = Cachorro("Rex", 5)
print("Pelo objeto:", dog.especie)
print("Pela classe:", Cachorro.especie)
