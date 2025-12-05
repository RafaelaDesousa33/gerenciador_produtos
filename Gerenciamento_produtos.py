from Produtos import Produtos


"""
Classe que irá fazer o gerenciamento de produtos:
- Cadastrar novos produtos
- Deletar produtos
- Calcular desconto
- Listar produtos
"""

class GerenciamentoProdutos:
   def __init__(self):
      self.lista_produtos = []
       


   def adicionar_produtos(self):
      while True:
         nome_input = input("Digite o nome do produto: ")
         preco_input = float(input("Digite o preço do produto: "))
         quantidade_input = int(input("Digite a quantidade: "))

         novo_produto = Produtos(nome_input, preco_input, quantidade_input)
         self.lista_produtos.append(novo_produto)
         
         print("Produto adicionado com sucesso!")
         break
       
   def listar_produtos(self):
      if len(self.lista_produtos) == 0:
         print("Nenhum produto encontrado.")
      else:
         for produto in self.lista_produtos:
            print(produto)

   def deletar_produto(self):
      produto_deletado = input("Digite o nome do produto que deseja excluir: ")

      for produto in self.lista_produtos:
         if produto.nome == produto_deletado:
            self.lista_produtos.remove(produto)
            print("Produto deletado com sucesso!")
            return 
      
      print("Produto não encontrado.")

   def calcular_desconto(self):
      for produto in self.lista_produtos:
         if produto.preco > 100:
            desconto = produto.preco * 0.10
            print(f"Desconto para {produto.nome}: R$ {desconto}")
            return
          
      print("Desconto só é validado se o preço do produto for maior que R$100.")


   def escolher_opcao(self):
      while True:
         escolha = input("Digite sua escolha (cadastrar, deletar, listar, calcular desconto, sair): ")

         if escolha == "cadastrar":
            self.adicionar_produtos()

         elif escolha == "deletar":
            self.deletar_produto()

         elif escolha == "listar":
            self.listar_produtos()

         elif escolha == "calcular desconto":
            self.calcular_desconto()

         elif escolha == "sair":
            print("Programa encerrado!")
            break

         else:
            print("Escolha inválida. Tente novamente.")
