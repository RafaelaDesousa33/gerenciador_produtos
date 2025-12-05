"""
 Gerenciador de Produtos

Conceitos: encapsulamento, validação de atributos.
Funcionalidades:

adicionar produto

alterar preço com setter

aplicar desconto automático via método

listar todos

"""

"""
    Classe que representa um produto com nome, preço e quantidade.
    Utiliza encapsulamento com propriedades (getters e setters)
    para garantir integridade dos dados.
    """

class Produtos:
    def __init__(self,nome,preco,quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    
    def __str__(self):
        return f"nome:{self.__nome}, preco:{self.__preco}, quantidade:{self.__quantidade}"

 
    #metodos getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    #metodos setters
    @nome.setter
    def nome(self,novo_nome):
        if len(novo_nome) > 0 and isinstance(novo_nome,str):
            self.__nome = novo_nome
        else:
            print("Erro: digite um nome valido")
        

    @preco.setter
    def preco(self,novo_preco):
        if novo_preco > 0 and isinstance(novo_preco, (float,int)):
            self.__preco = novo_preco
        else:
            print("Erro: preco negativo")

    @quantidade.setter
    def quantidade(self,nova_quantidade):
        if nova_quantidade >= 0 and isinstance(nova_quantidade,int):
            self.__quantidade = nova_quantidade
        else:
            print("Erro: quantidade negativa")

    
    
