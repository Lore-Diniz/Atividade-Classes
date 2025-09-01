# Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.

aluno = {
    "nome": "Loren",
    "idade": "22",
    "nota": "10"
}

# Imprima o nome do produto e a quantidade em estoque.



produto = {
    "nome": "Caneta",
    "Preço": "2.5",
    "Estoque": "100"
}

print(produto["nome"])
print(produto["Estoque"])

# Adicionando novos pares chave-valor


dicionario = {"nome": "Carlos", 
          "idade": 30}

dicionario.update({"cidade": "São Paulo"})
print(dicionario)

# Removendo elementos

carro = {"marca": "Ford", 
         "modelo": "Fiesta", 
         "ano": 2010}

carro.pop("ano")
print(carro)

# Verificando existência de uma chave

contato = {"nome": "Ana", 
           "email": "ana@email.com"}

if "telefone" in contato:
    print("Telefone já existe")
else:
    print("Telefone não existe")

# Contando frequência de palavras

palavras = ["maçã", 
            "banana", 
            "maçã", 
            "laranja", 
            "banana", 
            "maçã"]


def conte_palavras(palavras):
    numero = {}
    for palavra in palavras:  
        if palavra in numero:
            numero[palavra] += 1
        else:
            numero[palavra] = 1
    return numero


resultado = conte_palavras(palavras)
print(resultado)

# Invertendo um dicionário

d = {"a": 1, "b": 2, "c": 3}
inverted_d = {v: k for k, v in d.items()}
print(inverted_d)

# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

alunos = {
    "João": [8, 9, 9],
    "Mary": [7, 4, 8],
    "Luca": [9, 8, 7]
}

# Mesclando dois dicionários


for nome, nota in alunos.items():
    media = sum(nota) / len(nota)
    print(f"A média de {nome} é {media:.2f}")


dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}

def mesclar_dicts(dicionario1, dicionario2):
    resultado = dicionario1.copy()  
    resultado.update(dicionario2) 
    return resultado

novo = mesclar_dicts(dicionario1, dicionario2)
print(novo)

# Ordenando dicionário por valor

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
ordenar = dict(sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True))
print(ordenar)