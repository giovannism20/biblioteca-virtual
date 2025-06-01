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

    @staticmethod #Busca livros por campo, mantendo coesão via método estático
    def buscar_livros(campo, termo, livros, bibliotecas):
        resultados = []

        for titulo, livro in livros.items():
            if getattr(livro, campo).strip().lower() == termo.strip().lower():
                print(f"Livro encontrado: {titulo}")
                bibliotecas_encontradas = []

                for nome_biblioteca, biblioteca in bibliotecas.items():
                    for registro in biblioteca.livros:
                        if registro["livro"] == livro:
                            bibliotecas_encontradas.append(

                                (
                                    nome_biblioteca,
                                    registro["status"].name
                                )
                            )
                resultados.append((livro, bibliotecas_encontradas))

        if resultados:
            print(f"\n Resultado da busca por {campo} '{termo}':\n")
            for livro, lista_bibliotecas in resultados:
                print(f"  Título: {livro.titulo}")
                print(f"  Autor: {livro.autor}")
                print(f"  Gênero: {livro.genero}")
                print(f"  Edição: {livro.edicao}")
                print(f"  Série: {livro.serie}")
                print(f"  Páginas: {livro.paginas}")
                print(f"  Formato: {livro.formato}")
                if lista_bibliotecas:
                    print("  Bibliotecas onde está cadastrado:")
                    for nome, status in lista_bibliotecas:
                        print(f"  s- {nome} [{status}]")
                else:
                    print("  Sem vinculo a nenhuma biblioteca.\n")
        else:
            print(f"  Nenhum livro encontrado com {campo} '{termo}'.")
