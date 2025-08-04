# Caixa Eletrônico Simples

valor = int(input("Digite o valor que deseja sacar:"))

cedulas = [100,50,20,10,1]
notas   = []
resto   = valor

for cedula in cedulas:
    if cedula <= resto:
        notas.append({"nota": cedula, "qtd": resto // cedula})
        resto = valor % cedula
        print(resto)
        if resto == 0:
            break

print(notas)