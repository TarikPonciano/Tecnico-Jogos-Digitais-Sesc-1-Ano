class Livro:
    def __init__(self, nome, ndepaginas,autor,preco, editora):
        self.__nome = nome 
        self.ndepaginas = ndepaginas
        self.autor = autor  
        self.__preco = preco
        self.editora = editora

    def getPreco(self):
        return self.__preco
    def setPreco(self, novoPreco):
        if novoPreco > 0:
            self.__preco = novoPreco
    def setNome(self, novoNome):
        self.__nome = novoNome
    def mostrarInformacoes(self):
        
        print(f"""
              informacoes do livro
              nome:{self.__nome}
              paginas: {self.ndepaginas}
              autor: {self.autor}
              editora: {self.editora}
              preco: R$ {self.__preco:.2f}
              """)