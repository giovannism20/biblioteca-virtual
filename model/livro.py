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
