# estoque de mercado
# -> cadastro de produtos
#  -> nome do produto, marca, dt de compra, dt de validade, qtde
# -> listagem de estoque
# -> compra
#  -> escolher o produto a ser comprado (posso escolher vários) e a qtde do mesmo
#  -> subtrair a quantidade cadastrada pela quantidade comprada

estoque = []

while True:
    print("Bem vindo ao Estoque de Mercado!")
    print("1. Cadastrar produto.")
    print("2. Estoque.")
    print("3. Comprar produto.")
    print("4. Sair.")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        senha = input("Digite a senha para cadastrar: ")
        if senha == "cadastrar123":
            nome = input("Nome do produto: ")
            marca = input("Marca do produto: ")
            dt_compra = input("Data de compra (dd/mm/aaaa): ")
            dt_vali = input("Data de validade (dd/mm/aaaa): ")
            qtde = input("Quantidade: ")

            try:
                qtde = int(qtde)
                if qtde <= 0:
                    produto = [nome, marca, dt_compra, dt_vali, qtde]
                    estoque.append(produto)
                    print("Produto cadastrado com sucesso!")
            except ValueError:
                print("Quantidade inválida. Produto não cadastrado.")
            
        else:
            print("Senha incorreta. Cadastro não autorizado.")

    elif opcao == "2":
        if len(estoque) == 0:
            print("Estoque vazio.")
        else:
            print("Estoque Atual:")
            for i in range(len(estoque)):
                produto = estoque[i]
                print(f"{i}. {produto[0]} | Marca: {produto[1]} | Compra: {produto[2]} | Validade: {produto[3]} | Quantidade: {produto[4]}")

    elif opcao == "3":
        if len(estoque) == 0:
            print("Estoque vazio.")
        else:
            print("Produtos Disponíveis:")
            for i in range(len(estoque)):
                produto = estoque[i]
                print(f"{i}. {produto[0]} | Marca: {produto[1]} | Quantidade: {produto[4]}")

            fim = False
            while not fim:
                indice = input("Digite o número do produto você quer comprar (Ou digite -1 para sair): ")

                if indice == "-1":
                    fim = True
                else:
                    try:
                        indice = int(indice)
                        if 0 <= indice < len(estoque):
                            qtde_comprar = input("Quantidade que você quer comprar: ")
                            try:
                                qtde_comprar = int(qtde_comprar)
                                if qtde_comprar > 0:
                                    if estoque[indice][4] >= qtde_comprar:
                                        estoque[indice][4] -= qtde_comprar
                                        print("Compra realizada com sucesso!")
                                        if estoque[indice][4] == 0:
                                            print(f"Produto esgotado e removido do estoque.")