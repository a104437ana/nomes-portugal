#!/usr/bin/env python3
"""
Gera data/nomes_genero.json a partir de data/nomes.json: uma linha por nome
unico, em vez de uma linha por combinacao nome+genero. O campo "genero" passa
a poder ser "F", "M" ou "U" (unissexo, quando o nome aparece registado com os
dois generos em data/nomes.json).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOMES_PATH = ROOT / "data" / "nomes.json"
OUT_PATH = ROOT / "data" / "nomes_genero.json"


def main() -> None:
    nomes = json.loads(NOMES_PATH.read_text(encoding="utf-8"))

    generos_por_nome = {}
    for n in nomes:
        generos_por_nome.setdefault(n["nome"], set()).add(n["genero"])

    resultado = []
    for nome, generos in generos_por_nome.items():
        genero = "U" if len(generos) > 1 else next(iter(generos))
        resultado.append({"nome": nome, "genero": genero})

    resultado.sort(key=lambda e: (e["nome"].lower(), e["genero"]))

    OUT_PATH.write_text(
        json.dumps(resultado, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    unissexo = sum(1 for e in resultado if e["genero"] == "U")
    print(f"{len(resultado)} nomes unicos ({unissexo} unissexo) -> {OUT_PATH}")


if __name__ == "__main__":
    main()
