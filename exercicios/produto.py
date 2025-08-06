DESCONTO = 0.1

nomeProduto     = input("Nome do produto: ")
precoProduto    = float(input("Preço do produto: "))
quantidade      = int(input("Quantidade do produto: "))
valor           = precoProduto * quantidade
valorDesconto   = valor * DESCONTO
valorFinal      = valor - valorDesconto
print(f"Produto: {nomeProduto} \n"
      f"Quantidade: {quantidade} \n"
      f"Valor: {valor} \n"
      f"Valor do desconto: {valorDesconto} \n"
      f"Valor final: {valorFinal}")