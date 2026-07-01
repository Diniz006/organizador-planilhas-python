# Organizador de Planilhas em Python

Este projeto é uma automação simples feita em Python para limpar e organizar dados de uma planilha Excel.

## Objetivo

O objetivo do projeto é pegar uma planilha bagunçada, tratar os dados e gerar uma nova planilha organizada automaticamente.

O programa lê uma planilha de entrada, remove linhas vazias, padroniza colunas, limpa textos, corrige telefones e salva uma nova versão em Excel.

## Exemplo de problema resolvido

Antes da organização, uma planilha pode ter problemas como:

- Nomes de colunas com espaços extras
- E-mails com letras maiúsculas e minúsculas misturadas
- Status escritos de formas diferentes
- Telefones aparecendo em notação científica
- Linhas vazias
- Textos com espaços desnecessários

Depois da execução, os dados ficam padronizados e prontos para análise ou uso.

## Funcionalidades

- Lê uma planilha `.xlsx`
- Remove linhas completamente vazias
- Padroniza os nomes das colunas
- Remove espaços extras de textos
- Padroniza e-mails em letras minúsculas
- Padroniza status em letras minúsculas
- Corrige telefones para formato de texto
- Gera uma nova planilha organizada
- Exibe no terminal a planilha original e a planilha limpa

## Estrutura esperada

A pasta do projeto pode ficar assim:

```text
organizador_planilhas/
├── main.py
├── clientes_baguncados.xlsx
├── clientes_organizados.xlsx
└── README.md
```

## Como instalar as dependências

No terminal, dentro da pasta do projeto, execute:

```bash
pip install pandas openpyxl
```

Se o comando acima não funcionar, use:

```bash
python -m pip install pandas openpyxl
```

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

## Arquivo de entrada

O programa usa como entrada o arquivo:

```text
clientes_baguncados.xlsx
```

Esse arquivo representa uma planilha com dados desorganizados.

## Arquivo de saída

Após a execução, o programa gera o arquivo:

```text
clientes_organizados.xlsx
```

Esse arquivo contém os dados limpos e organizados.

## Exemplo de saída no terminal

```text
PLANILHA ORIGINAL
              Nome             EMAIL      Telefone   Valor Compra     Status
0        Ana Silva      ANA@EMAIL.COM  3.899999e+10          150.5      pago
1        João Souza    joao@email.com  3.898888e+10          200.0   PENDENTE
2               NaN               NaN           NaN            NaN        NaN
3   Maria Oliveira    MARIA@EMAIL.COM  3.897777e+10           99.9       Pago
4       Carlos Lima  carlos@email.com  3.896666e+10          350.0  pendente

--------------------------------------------------
PLANILHA LIMPA
             nome             email     telefone  valor_compra    status
0       Ana Silva     ana@email.com  38999990000         150.5      pago
1      João Souza    joao@email.com  38988880000         200.0  pendente
3  Maria Oliveira   maria@email.com  38977770000          99.9      pago
4     Carlos Lima  carlos@email.com  38966660000         350.0  pendente

--------------------------------------------------
Arquivo clientes_organizados.xlsx criado com sucesso!
```

## Tecnologias utilizadas

- Python
- pandas
- openpyxl

## Status do projeto

Projeto funcional em versão inicial.

## Possíveis melhorias futuras

- Permitir escolher o nome da planilha pelo terminal
- Gerar relatório com quantidade de linhas removidas
- Validar e-mails inválidos
- Identificar telefones incompletos
- Organizar os dados por status
- Criar uma interface simples
- Criar uma versão executável para Windows
