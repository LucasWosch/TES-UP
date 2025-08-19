# caractere é a menor unidade de um texto (pode ser letra, numero, espaço, pontuacao, simbolo, emoji)
# string é uma sequencia ordenada de caracteres

c1 = "A"
c2 = "ç"
c3 = " "
s1 = "Ana"
s2 = "Olá, mundo!"

print(len(c1))
print(len(c2))
print(len(c3))
print(len(s1))
print(len(s2))

print("----------------")
print(len("Lucas Gabriel Wosch Kania"))
print(len("Rio de Janeiro"))

# """ texto """ permitem textos de multi-linha


print("----------------")
print('Python')
print("Programação")
print("""Linha 1
Linha 2
Linha 3
""")


print("----------------")
print("Ele disse: 'Oi'")
print('Ele disse: "Oi"')
print("Ele disse: \"Oi\"")

print("----------------")
print("Data " + "Science")
print("ha" * 3)
print("Py" in "Python")
print("Java" not in "Python")

print("----------------")
print(len("casa"))
print(ord("L"))
print(ord("u"))
print(ord("c"))
print(ord("a"))
print(ord("s"))
print(ord("ç"))
print(chr(65))
print(chr(231))

print(chr(76))
print(chr(117))
print(chr(99))
print(chr(97))
print(chr(115))


print("----------------")
print("python".upper())
print("PYTHON".lower())
print("python".capitalize())
print("curso de python".title())


print("----------------")
s = "banana maça uva banana abacaxi banana"
print(s.count("banana"))
print(s.find("banana"))
print(s.rfind("banana"))
print(s.startswith("banana"))
print(s.endswith("banana"))


print("----------------")
s = "Ordem e Progresso"
print(s.replace("e", "&&"))
print(s.split())

items = ["a","b","c"]
print(" | ".join(items))


print("----------------")
nome = "Lucas"
idade = 21
curso = "BSI"
duracao_total = 4
ano_atual = 4

ano_restante = duracao_total - ano_atual

print(f"{nome} tem {idade} anos")
print(f"Falta {ano_atual} meses para {nome} terminar a faculdade")

print("----------------")
texto = "Relatório"
print(f"{texto:-^20}")
print(f"{texto:.<20}")
print(f"{texto:.>20}")


print("----------------")
produtos = []
valores = []
for produto in range(0,3):
    produtos.append({"nome": input("Digite o nome do produto:"),"valor": float(input("Digite o valor do produto:"))})

print("-" * 31)
print(f"{"Produto": <15} {"Preço": >15}")
print("-" * 31)
for produto in produtos:
    print(f"{"Produto " + produto["nome"]: <15} {produto["valor"]: >15}")

