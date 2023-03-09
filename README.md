# Teste Técnico - Neoway

Desenvolvimento back-end de um serviço de ETL na linguagem Python

O propósito desse serviço é ler o arquivo `base_teste.txt` e realizar validações dos dados contidos nas colunas de CPF e CNPJ. Após o tratamento dos dados, eles são armazenados no banco de dados PostgreSQL usando Docker.

## Para executar esse serviço, siga os passos abaixo:
> 1. Instale o Docker Desktop em sua máquina (caso ainda não tenha): 
> - [Docker](https://www.docker.com/products/docker-desktop)
> 2. Clonar o repositório e colar no terminal o seguinte comando:
> ```sh
> git clone git@github.com:anaelisaq/neoway-test.git
> ```
> 3. Executar o Docker Compose pelo terminal:
> ```sh
> docker-compose up -d
> ```
> 4. Em seguida, executar o comando no terminal para inicializr o serviço:
> ```sh
> docker-compose run app
> ```
>
>

## Para realização desse desenvolvimento, foram utilizadas as seguintes referências:

- [Validar CPF/CNPJ](https://www.alura.com.br/conteudo/python-validacao-dados#:~:text=Criando%20um%20novo%20Python%20file,contr%C3%A1rio%20o%20retorno%20ser%C3%A1%20False%20.)

- [Tratamento de erros em Python](https://www.alura.com.br/artigos/tratamento-de-excecoes-no-python)

- [PEP8](https://www.alura.com.br/conteudo/pep8-linters-python)

- [Conexão Postgres através do SQLAlchemy](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)

## Estrutura relacional do projeto

A partir desse serviço, será criada uma tabela chamada `dbneoway` e está armazenada de modo público no PostgreSQL, seguindo a estrutura relacional:

Column name                      | Data Type
---------------------------------|-----------
CPF                              | VARCHAR
PRIVATE                          | INTEGER
INCOMPLETO                       | INTEGER
DATA_DA_ULTIMA_COMPRA            | DATE
TICKET_MEDIO                     | FLOAT
TICKET_DA_ULTIMA_COMPRA          | FLOAT
LOJA_MAIS_FREQUENTE              | VARCHAR
LOJA_DA_ULTIMA_COMPRA            | VARCHAR
CPF_VALIDO                       | VARCHAR
CNPJ_LOJA_MAIS_FREQUENTE_VALIDO  | VARCHAR
CNPJ_LOJA_DA_ULTIMA_COMPRA_VALIDO| VARCHAR
