from controller.livro import cadastrar_livro, alterar_livro, excluir_livro, listar_livros_cadastrados
from data_store import livros, bibliotecas
from model.livro import Livro

def test_cadastrar_livro(monkeypatch):
    livros.clear()

    inputs = iter([
        "Contra-ataque perfeito", 
        "Olivia Ayres",
        "Romance com esporte",
        "1",
        "Garotas em quadra",
        "390",
        "Fisico"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    resultado = cadastrar_livro()

    assert "Contra-ataque perfeito" in livros
    assert isinstance(livros["Contra-ataque perfeito"], Livro)
    assert resultado == "O livro 'Contra-ataque perfeito' foi cadastrado com sucesso!"

def test_alterar_formato_livro(monkeypatch):
    livros.clear()

    livros["Livro Teste"] = Livro(
        titulo="Livro Teste",
        autor="Autor",
        genero="Gênero",
        edicao="1",
        serie="Série",
        paginas="100",
        formato="Físico"
    )

    monkeypatch.setattr("controller.livro.exibir_lista_livros", lambda _: {1: "Livro Teste"})

    monkeypatch.setattr("controller.livro.menu_altera_dados_livro", lambda livro: None)

    inputs = iter(["1", "7", "Digital"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    resultado = alterar_livro()

    assert livros["Livro Teste"].formato == "Digital"
    assert resultado == " Formato atualizado com sucesso."