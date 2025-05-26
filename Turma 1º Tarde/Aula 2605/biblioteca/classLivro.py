class Livro:
    def __init__(self, titulo, nroPaginas, genero, autor, anoLancamento):
        self.titulo = titulo
        if nroPaginas < 0:
            self.nroPaginas = "Não Especificado"
        else:
            self.nroPaginas = nroPaginas
        self.genero = genero
        self.autor = autor
        if anoLancamento > 2025:
            self.anoLancamento = "Lançamento Futuro"
        else: 
            self.anoLancamento = anoLancamento