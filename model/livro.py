class Livro:
    def __init__(self, **dados):
        self.titulo = dados.get("titulo", "Sem título")
        self.autor = dados.get("autor", "Desconhecido")
        self.genero = dados.get("genero", "Não especificado")
        self.edicao = dados.get("edicao", "Sem edição")
        self.serie = dados.get("serie", "Sem série")
        self.paginas = dados.get("paginas", 0)
        self.formato = dados.get("formato", "Desconhecido")

    def altera_titulo(self, novo_valor):
        self.titulo = novo_valor

    def altera_autor(self, novo_valor):
        self.autor = novo_valor

    def altera_genero(self, novo_valor):
        self.genero = novo_valor

    def altera_edicao(self, novo_valor):
        self.edicao = novo_valor

    def altera_serie(self, novo_valor):
        self.serie = novo_valor

    def altera_paginas(self, novo_valor):
        self.paginas = novo_valor

    def altera_formato(self, novo_valor):
        self.formato = novo_valor

    def __repr__(self):
        return f"{self.titulo}"
