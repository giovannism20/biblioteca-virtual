from pytest import CaptureFixture, MonkeyPatch
from controller.biblioteca import (
    cadastrar_biblioteca,
    alterar_nome_biblioteca,
    excluir_biblioteca,
    listar_bibliotecas_cadastradas,
)
from data_store import bibliotecas
from model.biblioteca import Biblioteca


def test_cadastrar_biblioteca(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _: "Biblioteca do Poyatos")
    bibliotecas.clear()
    resultado = cadastrar_biblioteca()
    assert "Biblioteca do Poyatos" in bibliotecas
    assert isinstance(bibliotecas["Biblioteca do Poyatos"], Biblioteca)
    assert (
        resultado == "A biblioteca 'Biblioteca do Poyatos' foi cadastrada com sucesso!"
    )


def test_alterar_nome_biblioteca(monkeypatch: MonkeyPatch):
    bibliotecas.clear()
    bibliotecas["Antiga"] = Biblioteca("Antiga")

    imputs = iter(["1", "Nova"])
    monkeypatch.setattr("builtins.input", lambda _: next(imputs))

    resultado = alterar_nome_biblioteca()

    assert "Antiga" not in bibliotecas
    assert "Nova" in bibliotecas
    assert resultado == "Nome da biblioteca alterado para 'Nova' com sucesso!"


def test_excluir_biblioteca(monkeypatch: MonkeyPatch):
    bibliotecas.clear()
    bibliotecas["Excluir"] = Biblioteca("Excluir")

    imputs = iter(["1", "s"])
    monkeypatch.setattr("builtins.input", lambda _: next(imputs))

    resultado = excluir_biblioteca()

    assert "Excluir" not in bibliotecas
    assert resultado == "Biblioteca 'Excluir' removida com sucesso."


def test_listar_bibliotecas_cadastradas(
    capfd: CaptureFixture[str], monkeypatch: MonkeyPatch
):
    bibliotecas.clear()
    bibliotecas["Biblioteca Azile"] = Biblioteca("Biblioteca Azile")

    resultado = listar_bibliotecas_cadastradas()
    out, err = capfd.readouterr()

    assert resultado == {1: "Biblioteca Azile"}
    assert "1 - Biblioteca Azile" in out
