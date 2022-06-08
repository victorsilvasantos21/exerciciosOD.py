import datetime


class Item:
  descricao = "" 
  data = None
  altura = 0.0
  
  def __init__(self, descricao, altura):
    self.descricao = descricao
    self.altura = altura
    self.data = datetime.datetime.now().date()

  def exibir_dados(self):
    print("Descrição item: ", self.descricao, "\nData criação: ", self.data.strftime("%d/%m/%Y"), "\nAltura do item: ", self.altura)
    


  # metodo de classe que exibe item de cenário em uma lista
  @staticmethod
  def exibir_lista_itens(lista):
    print("Exibindo itens da lista")
    for i in lista:
      i.exibir_dados()
      print("====================")

  @staticmethod
  def popular_lista_itens(lista):
    while (True):
      print("Cadastrando um item de cenário")
      descricao = input("Digite a descrição do item ou sair para finalizar o cadastro: ").upper() 
      if descricao == "SAIR":
        break
      altura = int(input("Digite a altura do item (cm): "))
      obj_item = Item(descricao, altura)
      lista.append( obj_item )
      print("=================================")