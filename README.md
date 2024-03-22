# Municípios que Aderiram à Operação Corta Fogo

[![Repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github&logoColor=f5f5f5)](https://github.com/open-focos/corta_fogo)
![Static Badge](https://img.shields.io/badge/Update-22.03.2024-blue?logo=Google%20Calendar&logoColor=white)

O Estado de São Paulo conta com o Sistema Estadual de Prevenção e Combate a Incêndios Florestais, criado pela [Lei Estadual nº 10.547, de 02 de maio de 2000](https://www.al.sp.gov.br/repositorio/legislacao/lei/2000/original-lei-10547-02.05.2000.html) e regulamentado pelo [Decreto Estadual nº 56.571, 22 de dezembro de 2010](https://www.al.sp.gov.br/repositorio/legislacao/decreto/2010/decreto-56571-22.12.2010.html).

O Sistema, que no período de junho de 2011 a maio de 2023 foi chamado de Operação Corta-Fogo, recebeu um novo nome e a partir de junho de 2023 passou a ser denominado de [Operação São Paulo Sem Fogo](https://semil.sp.gov.br/sma/sp-sem-fogo/). Dentre os objetivos da Operação, destacam-se os seguintes:

- Diminuir os focos de incêndio no estado;
- Reduzir as emissões de gases de efeito estufa (GEE) oriundas das queimadas;
- Proteger áreas com cobertura vegetal contra incêndios;
- Erradicar a prática irregular do uso do fogo, respeitando o disposto no Decreto Estadual nº 56.571/2010;
- Fomentar o desenvolvimento de alternativas ao uso do fogo para o manejo agrícola, pastoril e florestal.

<br>

---

## Lista Municípios

Nas _urls_ abaixo são apresentados os municípios que aderiram a Operação Corta Fogo.

- https://smastr16.blob.core.windows.net/cortafogo/sites/10/2020/10/municipios_aderentes_2020_outubro.pdf, foi esse arquivo que usei para converter em tabela
- https://smastr16.blob.core.windows.net/cortafogo/sites/10/2020/08/municipios_aderentes_2020_julho.pdf
- https://smastr16.blob.core.windows.net/cortafogo/sites/10/2022/07/lista_adesao_08-07-2022.pdf

<br>

Notei, em 2023, que não há mais uma maneira fácil de obter a listagem dos municípios que aderiram à Operação Corta-Fogo (ou Operação Sem-Fogo). Há um Power BI, onde é possível visualizar informação, porém sem possibilidade de extrair dados.

<br>

---

## Objetivo

O presente repositório visa organizar os _scripts_ para converter os arquivos em formato _.pdf_ em formato tabular.

- **_get_data.py_**, obtem os dados na _internet_ e faz o _download_ do arquivo _.pdf_.
- **_01_tabula.ipynb_**, lê o .pdf e converte para _.csv_, utilizando o _tabula_ ([PyPI](https://pypi.org/project/tabula-py/), [Read the Docs](https://tabula-py.readthedocs.io/en/latest/))
- **_02_pdfplumber.ipynb_**, lê o .pdf e converte para _.csv_, utilizando o _pdfplumber_ ([PyPI](https://pypi.org/project/pdfplumber/), [Read the Docs](https://github.com/jsvine/pdfplumber))

<br>

---

## Requisitos

Para usar o _tabula_ é necessário instalar o Java Runtime

```shell
choco install javaruntime
```
