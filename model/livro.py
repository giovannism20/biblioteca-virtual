class Livro:
    def __init__(self, **dados):
        self.titulo = dados.get("titulo", "Sem título")
        self.autor = dados.get("autor", "Desconhecido")
        self.genero = dados.get("genero", "Não especificado")
        self.edicao = dados.get("edicao", "Sem edição")
        self.serie = dados.get("serie", "Sem série")
        self.paginas = dados.get("paginas", 0)
        self.formato = dados.get("formato", "Desconhecido")

    def __repr__(self):
        return f"{self.titulo}"

    def altera_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def consulta_titulo(self):
        return self.titulo

    def altera_autor(self, novo_autor):
        self.autor = novo_autor

    def consulta_autor(self):
        return self.autor

    def altera_genero(self, novo_genero):
        self.genero = novo_genero

    def consulta_genero(self):
        return self.genero

    def altera_edicao(self, novo_edicao):
        self.edicao = novo_edicao

    def consulta_edicao(self):
        return self.edicao

    def altera_serie(self, novo_serie):
        self.serie = novo_serie

    def consulta_serie(self):
        return self.serie

    def altera_paginas(self, novo_paginas):
        self.paginas = novo_paginas

    def consulta_paginas(self):
        return self.paginas

    def altera_formato(self, novo_formato):
        self.formato = novo_formato

    def consulta_formato(self):
        return self.formato

