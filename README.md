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

Para realização desse desenvolvimento, foram utilizadas as seguintes bibliotecas

vallidar cpf/cnpj https://www.alura.com.br/conteudo/python-validacao-dados#:~:text=Criando%20um%20novo%20Python%20file,contr%C3%A1rio%20o%20retorno%20ser%C3%A1%20False%20.

pacote de validação documentos br https://github.com/alvarofpp/validate-docbr