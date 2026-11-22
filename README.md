# RentSmart — Sistema de Orçamento de Locação

**Disciplina:** Algorithmic Thinking & Introduction to Object-Oriented Programming  
**Aluno:** Vitor da Silva Sá  
**RA:** 232306

## Sobre o projeto

O **RentSmart** é uma aplicação em Python desenvolvida para simular orçamentos de locação da imobiliária fictícia **R.M Imóveis**. O sistema recebe informações sobre o imóvel, calcula o aluguel mensal com seus adicionais e descontos, apresenta a taxa contratual separadamente e gera um arquivo CSV com a projeção dos pagamentos dos primeiros 12 meses.

O projeto aplica pensamento algorítmico e conceitos de **Programação Orientada a Objetos (POO)** para organizar as regras de negócio e os cálculos.

## Funcionalidades

- Escolha entre apartamento, casa ou estúdio.
- Definição de quartos e vagas de garagem ou estacionamento, conforme o tipo de imóvel.
- Cálculo automático de adicionais e desconto quando aplicável.
- Parcelamento da taxa contratual em 1 a 5 vezes.
- Validação das principais opções informadas pelo usuário.
- Exibição detalhada do orçamento no terminal.
- Geração do arquivo `projecao_12_meses.csv`, com aluguel, parcela da taxa e total de cada mês.

## Regras de negócio

| Tipo de imóvel | Aluguel-base | Adicionais |
| --- | ---: | --- |
| Apartamento | R$ 700,00 | Segundo quarto: R$ 200,00; uma vaga: R$ 300,00 |
| Casa | R$ 900,00 | Segundo quarto: R$ 250,00; uma vaga: R$ 300,00 |
| Estúdio | R$ 1.200,00 | Pacote inicial de duas vagas: R$ 250,00; cada vaga extra: R$ 60,00 |

- **Desconto:** apartamentos sem crianças recebem 5% de desconto sobre o aluguel-base somado aos adicionais.
- **Taxa contratual:** R$ 2.000,00, parcelável de 1 a 5 vezes. As parcelas são cobradas apenas nos meses correspondentes.
- **Estúdio:** o estacionamento é opcional; quando contratado, começa com um pacote de duas vagas. O programa não oferece uma única vaga avulsa.

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão `csv` — gravação da projeção em CSV.
- Biblioteca padrão `decimal` — cálculos monetários com `Decimal`.
- Biblioteca padrão `pathlib` — definição do caminho do arquivo gerado.

**Não é necessário instalar dependências com `pip`.**

## Como executar

1. Instale o [Python 3](https://www.python.org/downloads/), caso ainda não esteja instalado.
2. Baixe o arquivo `rentsmart.py` deste repositório.
3. Abra um terminal na pasta onde está o arquivo.
4. Execute:

   ```bash
   python rentsmart.py
   ```

   No Windows, caso o comando `python` não seja reconhecido, tente:

   ```bash
   py rentsmart.py
   ```

5. Responda às perguntas exibidas no terminal sobre o tipo de imóvel, quartos, vagas, crianças (quando aplicável) e parcelas da taxa contratual.
6. Confira o resumo do orçamento. O arquivo `projecao_12_meses.csv` será criado ou atualizado na mesma pasta do programa.

## Exemplo de orçamento

Para um **apartamento de dois quartos, uma vaga de garagem, sem crianças e taxa contratual em quatro parcelas**:

| Item | Valor |
| --- | ---: |
| Aluguel-base | R$ 700,00 |
| Segundo quarto | + R$ 200,00 |
| Garagem | + R$ 300,00 |
| Desconto de 5% | − R$ 60,00 |
| **Aluguel mensal** | **R$ 1.140,00** |
| Taxa contratual | R$ 2.000,00 |
| Parcela da taxa (4 vezes) | R$ 500,00 |
| **Total mensal nos meses 1 a 4** | **R$ 1.640,00** |
| **Total mensal nos meses 5 a 12** | **R$ 1.140,00** |

O CSV contém as colunas **Mês**, **Aluguel mensal (R$)**, **Parcela da taxa (R$)** e **Total do mês (R$)**, para os 12 meses da projeção.

## Organização do código e orientação a objetos

O arquivo `rentsmart.py` contém duas classes principais:

- **`Imovel`**: guarda categoria, quartos, vagas e condição sobre crianças. Seus métodos calculam aluguel-base, adicionais, desconto e aluguel mensal; o construtor valida combinações inválidas.
- **`Orcamento`**: guarda o imóvel e a quantidade de parcelas, calcula a parcela da taxa contratual, obtém os valores de cada mês e gera o CSV.

A função `main()` organiza a interação com o usuário. Funções auxiliares validam as entradas e formatam os valores monetários.

Essa divisão permite separar as responsabilidades, reutilizar os cálculos e evitar repetição desnecessária de código.

## Arquivos do projeto

```text
RentSmart/
├── rentsmart.py               # Aplicação em Python
├── projecao_12_meses.csv      # Exemplo de projeção / arquivo gerado na execução
├── README.md                  # Instruções e documentação resumida
└── RentSmart_...pdf           # Documentação teórica (se adicionada ao repositório)
```

> **Atenção:** executar o programa novamente sobrescreve `projecao_12_meses.csv` com os dados do novo orçamento.

## Objetivo acadêmico

Atividade desenvolvida para a disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**, demonstrando análise de problemas, validação de entradas, estruturas de decisão, repetição, classes, objetos, atributos, métodos e geração de arquivos CSV.
