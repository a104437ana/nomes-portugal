#!/usr/bin/env python3
"""
Extrai a lista de nomes do PDF oficial do IRN e gera data/nomes.json.

Fonte: https://irn.justica.gov.pt/Portals/33/Regras%20Nome%20Proprio/Lista%20Nomes%20Pr%C3%B3prios.pdf
Formato do PDF: duas colunas (Femininos | Masculinos), uma entrada "Género Nome"
por coluna e por linha, repetidas ao longo de 88 páginas.

Requer poppler-utils (comando `pdftotext`).
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = ROOT / "data" / "Lista_Nomes_Proprios.pdf"
OUT_PATH = ROOT / "data" / "nomes.json"

SKIP_MARKERS = ("Instituto dos Registos", "Campus de Justiça", "GÉNERO")

# Nomes compostos longos que o PDF quebra em duas linhas visuais, perdendo
# a segunda parte na extração em texto. Correção manual dos casos conhecidos.
KNOWN_FIXES = {
    ("Darius", "M"): "Darius-Alexandru",
}


def extract_text(pdf_path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def parse(text: str) -> list[dict]:
    entries = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or any(marker in line for marker in SKIP_MARKERS):
            continue
        tokens = line.split()
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            if tok in ("Femininos", "Masculinos") and i + 1 < len(tokens):
                genero = "F" if tok == "Femininos" else "M"
                nome = tokens[i + 1]
                nome = KNOWN_FIXES.get((nome, genero), nome)
                entries.append({"nome": nome, "genero": genero})
                i += 2
            else:
                i += 1
    return entries


def dedupe_and_sort(entries: list[dict]) -> list[dict]:
    seen = set()
    unique = []
    for e in entries:
        key = (e["nome"], e["genero"])
        if key not in seen:
            seen.add(key)
            unique.append(e)
    unique.sort(key=lambda e: (e["nome"].lower(), e["genero"]))
    return unique


def main() -> None:
    if not PDF_PATH.exists():
        sys.exit(f"PDF não encontrado em {PDF_PATH}")
    text = extract_text(PDF_PATH)
    entries = dedupe_and_sort(parse(text))
    OUT_PATH.write_text(
        json.dumps(entries, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    fem = sum(1 for e in entries if e["genero"] == "F")
    mas = sum(1 for e in entries if e["genero"] == "M")
    print(f"{len(entries)} nomes ({fem} femininos, {mas} masculinos) -> {OUT_PATH}")


if __name__ == "__main__":
    main()
