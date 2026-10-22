# nomes-portugal

Site estático para pesquisar e filtrar a lista de nomes próprios do IRN (Instituto dos Registos e do Notariado).

Não é um site oficial do IRN.

## Usar

Abrir `index.html` no browser. Não precisa de build nem de servidor.

## Dados

- `data/Lista_Nomes_Proprios.pdf` — documento oficial do IRN, de 2021.
- `data/nomes.json` — gerado por `scripts/parse_pdf.py` a partir do PDF. Extrai as duas colunas do documento (Femininos/Masculinos) para uma lista de objetos `{"nome": ..., "genero": "F"|"M"}`. Nomes unissexo aparecem duas vezes aqui, uma por género.
- `data/nomes_genero.json` — gerado por `scripts/unificar_genero.py` a partir de `nomes.json`. Tem uma linha por nome único, com o campo `genero`: `F` (feminino), `M` (masculino) ou `U` (unissexo, quando o nome está registado com os dois géneros). É este ficheiro que o `index.html` usa.

Para regenerar os dados a partir do PDF:

```bash
python3 scripts/parse_pdf.py
python3 scripts/unificar_genero.py
```

