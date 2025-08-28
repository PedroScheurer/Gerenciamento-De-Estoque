from Estruturas.Lista import LDE
from Estruturas.Pilha import Pilha
from Estruturas.Fila import Fila
from Produto import Produto
from Cliente import Cliente
import os, sys, time
os.system('cls')

historico = Pilha()

produto = Produto()
cliente = Cliente()
id_produto = 0
id_cliente = 0

while True:

    print("\n-------- MENU ESTOQUE --------")
    print("Seja bem-vindo! Como podemos te ajudar hoje?")
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    # pesquisar produtos por nome ou ID
    print("3 - Cadastrar cliente")
    print("4 - Listar clientes")
    print("5 - Realizar venda")
    print("6 - Ver fila de vendas")
    print("7 - Exibir valor total do estoque")
    print("8 - Exibir valor total de vendas realizadas")
    print("9 - Exibir clientes e valores totais gastos")
    print("10 - Desfazer última operação (cadastro/venda)")
    print("11 - Sair")
    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        os.system("cls")
        print("\n-------- CADASTRO DE PRODUTO --------")
        while True:
            nome_produto = input("\nDigite o nome do produto: ").strip().title()
            if all(palavra.isalpha() for palavra in nome_produto.split()):
                break
            else:
                print("Nome inválido! Digite apenas letras e espaços.")
        while True:
            qtd_input = input("Digite a quantidade do produto: ").strip()
            if qtd_input.isdigit():  
                quantidade_produto = int(qtd_input)
                if quantidade_produto > 0:
                    break
                else:
                    print("A quantidade deve ser maior que zero.")
            else:
                print("Entrada inválida! Digite apenas números inteiros.")
        while True:
            preco_input = input("Digite o preço unitário do produto: ").strip()
            try:
                preco_produto = float(preco_input)
                if preco_produto < 0:
                    print("O preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números (use ponto para decimais - Ex: 12.50).")
        id_produto += 1 
        print(f"\nProduto '{nome_produto}' cadastrado com sucesso!")
        print(f"Identificador do produto: {id_produto}")
        produto.cadastrar_produto(nome_produto, quantidade_produto, preco_produto, id_produto)

    elif opcao == 2:
        os.system("cls")
        print("\n---- PRODUTOS CADASTRADOS ----")
        produto.listar_produtos()

    elif opcao == 3:
        os.system("cls")
        print("\n-------- CADASTRO DE CLIENTE --------")
        while True:
            nome_cliente = input("\nDigite o nome do cliente: ").strip().title()
            if all(palavra.isalpha() for palavra in nome_cliente.split()):
                break
            else:
                print("Nome inválido! Digite apenas letras e espaços.")
        id_cliente += 1 
        print(f"\nCliente '{nome_cliente}' cadastrado com sucesso!")
        print(f"Identificador do cliente: {id_cliente}")
        cliente.cadastrar_cliente(id_cliente, nome_cliente)

    elif opcao == 4:
        os.system("cls")
        print("\n---- CLIENTES CADASTRADOS ----")
        cliente.listar_cliente()

        '''elif opcao == 5:
            os.system("cls")
            print("\n-------- REALIZAR VENDA --------")
            comprador = input("\nInforme o ID do cliente: ")
            id_produto = input("\nDigite o ID do produto: ")
            quantidade_vendida = int(input("\nDigite a quantidade: "))
            preco_produto = produto.buscar_preco_produto(id_produto)
            valor_total = quantidade_vendida * preco_produto
            print(f"\nVenda de '{quantidade_vendida}' '{id_produto}' para '{comprador}' realizada com sucesso!")  #id_produto = nome do produto e comprador = nome do cliente
            print(f"Valor total da venda: {valor_total:.2f}") 
            os.system("cls")
            produto.realizar_venda(id_cliente, id_produto, quantidade_vendida)'''

    elif opcao == 6:
        os.system("cls")
        print("\n-------- FILA DE VENDAS --------")
        pass

    elif opcao == 7:
        os.system("cls")
        print("\n-------- VALOR TOTAL DO ESTOQUE --------")
        produto.exibir_valor_total_estoque()
        input("\nPressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 8:
        os.system("cls")
        print("\n-------- VALOR TOTAL DE VENDAS --------")

    elif opcao == 9:
        os.system("cls")
        print("\n-------- CLIENTES E VALORES TOTAIS GASTOS --------")
        pass

    elif opcao == 10:
        os.system("cls")
        print("\n-------- DESFAZER ÚLTIMA OPERAÇÃO --------")
        pass

    elif opcao == 11:
        print("\nOperação finalizada. Agradecemos a sua confiança.")
        time.sleep(2)
        os.system("cls")
        sys.exit()