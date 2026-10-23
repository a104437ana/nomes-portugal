# nomes-portugal

Site estático para pesquisar e filtrar a lista de nomes próprios, baseado no [documento oficial do IRN](https://irn.justica.gov.pt/Portals/33/Regras%20Nome%20Proprio/Lista%20Nomes%20Pr%C3%B3prios.pdf?ver=WNDmmwiSO3uacofjmNoxEQ%3D%3D), de 2021.

**Site:** https://nomes-portugal.vercel.app

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

## Stars
[![a104437ana/nomes-portugal stars](https://repo-stars.vercel.app/api/stars-badge?repo=a104437ana%2Fnomes-portugal)](https://repo-stars.vercel.app)
[![a104437ana/nomes-portugal stars](https://repo-stars.vercel.app/api/svg?repo=a104437ana%2Fnomes-portugal)](https://repo-stars.vercel.app)

---

<a href="https://star-history.com/#a104437ana/nomes-portugal&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=a104437ana/nomes-portugal&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=a104437ana/nomes-portugal&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=a104437ana/nomes-portugal&type=Date" />
  </picture>
</a>
