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
valor_total_vendas = 0

def ler_inteiro(prompt):
    while True:
        valor = input(prompt).strip()
        if valor.isdigit():
            return int(valor)
        print("Digite apenas números inteiros válidos!")

def ler_float(prompt):
    while True:
        valor = input(prompt).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Digite um valor numérico válido!")

while True:
    try:
        print("\n-------- MENU ESTOQUE --------")
        print("Seja bem-vindo! Como podemos te ajudar hoje?")
        print("\n1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Cadastrar cliente")
        print("4 - Listar clientes")
        print("5 - Realizar venda")
        print("6 - Ver fila de vendas")
        print("7 - Exibir valor total do estoque")
        print("8 - Exibir valor total de vendas realizadas")
        print("9 - Exibir clientes e valores totais gastos")
        print("10 - Desfazer última operação (cadastro/venda)")
        print("11 - Pesquisar produto por nome ou ID")
        print("12 - Salvar estoque em arquivo")
        print("13 - Carregar estoque de arquivo")
        print("14 - Sair")

        opcao = ler_inteiro("\nDigite a opção desejada: ")

        if opcao == 1:
            os.system("cls")
            nome_produto = input("\nDigite o nome do produto: ").strip().title()
            quantidade_produto = ler_inteiro("Digite a quantidade do produto: ")
            preco_produto = ler_float("Digite o preço unitário do produto: ")
            id_produto += 1 
            produto.cadastrar_produto(nome_produto, quantidade_produto, preco_produto, id_produto)
            historico.inserir({
                "acao": "cadastro_produto",
                "dados": {"id": id_produto, "nome": nome_produto}
            })
            print(f"\nProduto '{nome_produto}' cadastrado com sucesso! (ID: {id_produto})")
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 2:
            os.system("cls")
            produto.listar_produtos()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 3:
            os.system("cls")
            nome_cliente = input("\nDigite o nome do cliente: ").strip().title()
            id_cliente += 1 
            cliente.cadastrar_cliente(id_cliente, nome_cliente)
            historico.inserir({
                "acao": "cadastro_cliente",
                "dados": {"id": id_cliente, "nome": nome_cliente}
            })
            print(f"\nCliente '{nome_cliente}' cadastrado com sucesso! (ID: {id_cliente})")
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 4:
            os.system("cls")
            cliente.listar_cliente()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 5:
            os.system("cls")
            id_cliente_venda = ler_inteiro("\nInforme o ID do cliente: ")
            cliente_encontrado = cliente.buscar_cliente(id_cliente_venda)
            if cliente_encontrado is None:
                print("Cliente não encontrado.")
                input("\nPressione ENTER para voltar ao menu...")
                continue
            id_produto_venda = ler_inteiro("\nDigite o ID do produto: ")
            produto_encontrado = produto.buscar_produto(id_produto_venda)
            if produto_encontrado is None:
                print("Produto não encontrado.")
                input("\nPressione ENTER para voltar ao menu...")
                continue
            quantidade_vendida = ler_inteiro("\nDigite a quantidade: ")
            if quantidade_vendida <= 0 or quantidade_vendida > produto.buscar_quantidade_produto(id_produto_venda):
                print("Quantidade inválida ou não disponível em estoque.")
                input("\nPressione ENTER para voltar ao menu...")
                continue
            venda_sucesso = produto.realizar_venda(id_cliente_venda, id_produto_venda, quantidade_vendida, cliente)
            if venda_sucesso:
                valor_total = quantidade_vendida * produto.buscar_preco_produto(id_produto_venda)
                valor_total_vendas += valor_total
                historico.inserir({
                    "acao": "venda",
                    "dados": {
                        "id_cliente": id_cliente_venda,
                        "id_produto": id_produto_venda,
                        "quantidade": quantidade_vendida,
                        "valor": valor_total
                    }
                })
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 6:
            os.system("cls")
            produto.vendas.imprimir()
            input("\nPressione ENTER para continuar...")

        elif opcao == 7:
            os.system("cls")
            produto.exibir_valor_total_estoque()
            input("\nPressione ENTER para continuar...")

        elif opcao == 8:
            os.system("cls")
            print(f"R$ {valor_total_vendas:.2f}")
            input("\nPressione ENTER para continuar...")       

        elif opcao == 9:
            os.system("cls")
            cliente.listar_clientes_com_gastos()
            input("\nPressione ENTER para continuar...")

        elif opcao == 10:
            os.system("cls")
            ultima = historico.remover()
            if not ultima:
                print("Nenhuma operação para desfazer.")
            else:
                acao = ultima["acao"]
                dados = ultima["dados"]
                if acao == "cadastro_produto":
                    produto.remover_produto(dados["id"])
                    print(f"Desfeito: cadastro do produto '{dados['nome']}'")
                elif acao == "cadastro_cliente":
                    cliente.remover_cliente(dados["id"])
                    print(f"Desfeito: cadastro do cliente '{dados['nome']}'")
                elif acao == "venda":
                    produto.estornar_venda(dados, cliente)
                    valor_total_vendas -= dados["valor"]
                    print("Desfeito: última venda.")
            input("\nPressione ENTER para continuar...")

        elif opcao == 11:
            termo = input("Digite o nome ou ID do produto: ").strip()
            if termo.isdigit():
                produto_encontrado = produto.buscar_produto(int(termo))
                if produto_encontrado:
                    print(f"ID: {produto_encontrado['id']} | Nome: {produto_encontrado['nome']} | Quantidade: {produto_encontrado['quantidade']} | Preço: R$ {produto_encontrado['preco']:.2f}")
                else:
                    print("Produto não encontrado pelo ID.")
            else:
                encontrados = [p for p in produto.produtos if termo.lower() in p['nome'].lower()]
                if encontrados:
                    for p in encontrados:
                        print(f"ID: {p['id']} | Nome: {p['nome']} | Quantidade: {p['quantidade']} | Preço: R$ {p['preco']:.2f}")
                else:
                    print("Nenhum produto encontrado com esse nome.")
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 12:
            produto.salvar_estoque()
            print("Estoque salvo em 'estoque.txt'.")
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 13:
            produto.carregar_estoque()
            if produto.produtos:
                id_produto = max(p['id'] for p in produto.produtos)
            else:
                id_produto = 0
            print("Estoque carregado de 'estoque.txt'.")
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == 14:
            print("\nOperação finalizada. Agradecemos a sua confiança.")
            time.sleep(2)
            sys.exit()

        else:
            print("Opção inválida. Digite um número entre 1 e 14.")

    except Exception as e:
        print(f"ERRO\n{e}")



