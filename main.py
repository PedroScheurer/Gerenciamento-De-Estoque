from Estruturas.Lista import LDE
from Estruturas.Pilha import Pilha
from Estruturas.Fila import Fila
from Produto import Produto
import os
os.system('cls')

vendas = Fila()
historico = Pilha()
produto = Produto()
contador = 0

while True:

    print("\n-------- MENU ESTOQUE --------")
    print("Seja bem-vindo! Como podemos te ajudar hoje?")
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Realizar venda")
    print("4 - Ver fila de vendas")
    print("5 - Desfazer última operação")
    print("6 - Exibir valor total do estoque")
    print("7 - Exibir valor total de vendas realizadas")
    print("8 - Sair")
    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        os.system("cls")
        print("\n-------- CADASTRO DE PRODUTO --------")
        nome_produto = input("\nDigite o nome do produto: ")   
        quantidade_produto = int(input("Digite a quantidade do produto: "))
        preco_produto = float(input("Digite o preço do produto: "))
        id_produto = contador + 1
        contador += 1 
        print(f"\nProduto '{nome_produto}' cadastrado com sucesso!")
        print(f"Identificador do produto: {id_produto}")
        produto.cadastrar_produto(nome_produto, quantidade_produto, preco_produto, id_produto)

    elif opcao == 2:
        os.system("cls")
        print("\n----PRODUTOS CADASTRADOS----")
        produto.listar_produtos()

    elif opcao == 3:
        os.system("cls")
        print("\n-------- REALIZAR VENDA --------")
        produto_vendido = input("\nDigite o ID do produto: ")
        quantidade_vendida = int(input("Digite a quantidade: "))
        print(f"\nVenda do produto '{produto_vendido}' realizada com sucesso!")
        print(f"Valor total da venda: {quantidade_vendida * 10}") 
        os.system("cls")
        Produto.realizar_venda(produto_vendido, quantidade_vendida)

    elif opcao == 4:
        os.system("cls")
        print("\n-------- FILA DE VENDAS --------")
        pass

    elif opcao == 5:
        os.system("cls")
        print("\n-------- DESFAZER ÚLTIMA OPERAÇÃO --------")
        pass

    elif opcao == 6:
        os.system("cls")
        print("\n-------- VALOR TOTAL DO ESTOQUE --------")
        pass

    elif opcao == 7:
        os.system("cls")
        print("\n-------- VALOR TOTAL DE VENDAS --------")
        pass

    elif opcao == 8:
        os.system("cls")
        print("Obrigado por usar nosso sistema!")
        break