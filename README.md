# Olimpíadas API

## Descrição
Projeto desenvolvido como parte do desafio Celero - back-end.

A API tem por objetivo reunir dados sobre os atletas e resultados das Olimpíadas, e foi desenvolvida tendo como base os dados do dataset ["120 years of Olympic history: athletes and results"](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results).

O diagrama entidade-relacionamento pode ser encontrado [aqui](der.png).

## Configuração do projeto

### Tecnologias

A API foi inteiramente desenvolvida usando Python 3.7, com o framework Django REST Framework 3.12.4. O banco de dados escolhido foi o PostgreSQL 13.3.

### Instruções de execução

Primeiramente, após clonar o repositório, é preciso criar o ambiente virtual e instalar as dependências do projeto Python:
> python -m venv venv
> 
> pip install -r requirements.txt

Após isso, na raiz do [projeto Django](desafiocelero), crie um novo arquivo chamado local_settings.py e faça as configurações do banco de dados nesse arquivo criado. É possível encontrar um arquivo de exemplo em [desafiocelero/local_settings_sample.py](desafiocelero/local_settings_sample.py). A SECRET_KEY necessária para o projeto pode ser tanto adicionada nesse arquivo quanto nas variáveis de ambiente!

Então, efetue a migração dos models e das importações necessárias:
> python manage.py migrate

Para iniciar o projeto, utilize o seguinte comando:
> python manage.py runserver

Após iniciar o projeto, é possível encontrar uma documentação detalhada de todas as rotas da API na seguinte URL:
> http://localhost:8000

### Importações

Caso deseje, é possível fazer a importação do dataset "120 years of Olympic history: athletes and results" utilizando o seguinte comando:
> python manage.py extract_athletes file_path

Sendo "file_path" substituído pelo caminho do CSV no seu computador.

### Docker

O projeto possui configurações para criar o container do banco de dados! Caso deseje utilizá-lo, na raiz do projeto crie um arquivo chamado .env e adicione as variáveis necessárias. É possível encontrar um arquivo de exemplo em [.env_example](.env_example). Após a criação desse arquivo, rode o seguinte comando:
> docker-compose up -d db

Após criação do container, lembre de configurar o banco de dados criado ao projeto, como explicado no passo "Instruções de execução"!



