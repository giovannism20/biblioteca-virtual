from pytest import MonkeyPatch
from controller.livro import (
    cadastrar_livro,
    alterar_livro,
    excluir_livro,
    listar_livros_cadastrados,
    pesquisar_livro,
)
from data_store import livros, bibliotecas
from model.livro import Livro


def test_cadastrar_livro(monkeypatch: MonkeyPatch):
    livros.clear()

    inputs = iter(
        [
            "Contra-ataque perfeito",
            "Olivia Ayres",
            "Romance com esporte",
            "1",
            "Garotas em quadra",
            "390",
            "Fisico",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    resultado = cadastrar_livro()

    assert "Contra-ataque perfeito" in livros
    assert isinstance(livros["Contra-ataque perfeito"], Livro)
    assert resultado == "O livro 'Contra-ataque perfeito' foi cadastrado com sucesso!"


def test_alterar_formato_livro(monkeypatch: MonkeyPatch):
    livros.clear()

    livros["Livro Teste"] = Livro(
        titulo="Livro Teste",
        autor="Autor",
        genero="Gênero",
        edicao="1",
        serie="Série",
        paginas="100",
        formato="Físico",
    )

    monkeypatch.setattr(
        "controller.livro.exibir_lista_livros", lambda _: {1: "Livro Teste"}
    )

    monkeypatch.setattr("controller.livro.menu_altera_dados_livro", lambda livro: None)

    inputs = iter(["1", "7", "Digital"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    resultado = alterar_livro()

    assert livros["Livro Teste"].formato == "Digital"
    assert resultado == " Formato atualizado com sucesso."


class BibliotecaMock:
    def remover_livro(self, livro):
        pass  # simula método sem efeito colateral


def test_excluir_livro(monkeypatch: MonkeyPatch):
    livros.clear()
    bibliotecas.clear()

    livros["Livro Teste"] = Livro(
        titulo="Livro Teste",
        autor="Autor",
        genero="Gênero",
        edicao="1",
        serie="Série",
        paginas="100",
        formato="Físico",
    )

    bibliotecas["Central"] = BibliotecaMock()

    monkeypatch.setattr(
        "controller.livro.exibir_lista_livros", lambda _: {1: "Livro Teste"}
    )

    inputs = iter(["1", "s"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    resultado = excluir_livro()

    assert "Livro Teste" not in livros
    assert resultado == " Livro 'Livro Teste' excluído com sucesso."


def test_listar_livros():
    livros.clear()
    resultado = listar_livros_cadastrados()
    assert resultado == "Ainda não há livros cadastrados."


def test_pesquisar_livro(monkeypatch: MonkeyPatch):
    livros.clear()
    bibliotecas.clear()

    livros["Python Clean"] = Livro(
        titulo="Python Clean",
        autor="Autor X",
        genero="Tech",
        edicao="1",
        serie="A",
        paginas="200",
        formato="Digital",
    )

    monkeypatch.setattr("controller.livro.menu_busca_livro", lambda: None)

    inputs = iter(["1", "Python Clean"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr(
        "controller.livro.buscar_livros",
        lambda campo, termo, _, __: f"Simulado: {campo} = {termo}",
    )

    resultado = pesquisar_livro()

    assert resultado == "Simulado: titulo = Python Clean"
