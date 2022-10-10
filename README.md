# Panificadora Gustapão / Bakery Gustapão (en)

# Instruções:
## Crie o ambiente virtual
```
python -m venv venv
source venv/bin/activate
```
## Ative o venv

### Instale as dependências

```
pip install -r requirements.txt
```

## Rodando / Run:

## Docker-compose
Nota: Crie um arquivo .env de acordo com o .env.example
```
docker-compose up 
#depois de rodar, acesse o shell do web e rode as migrations
./manage.py migrate
```

## Sqlite3

```
TEST=TEST ./manage.py migrate
TEST=TEST ./manage.py runserver
```

# PostgreSQL
Nota: Crie um banco de dados e adicione as informações ao .env de acordo com o .env.example

```
./manage.py migrate
./manage.py runserver
```

### Este projeto visa ajudar uma panificadora localizada em Curitiba, Brasil, que poossui um excelente atendimento e comidas, porém, não possui um sistema dedicado ao gerenciamento de pedidos.

### (en) This project aims to help a bakery located in Curitiba, Brazil, which has excellent service and food, but does not have a dedicated order management system.

Team: 
Alysson Marcos Colombo - alysson1346 - SCRUM Master <br>
João Francisco Guarda Pozzer - joaofranciscoguarda - Tech Leader <br>
Régis Theobald Silveira - xregizzz - Product Owner <br>
Kennedy Melo Barreto Muniz - kennedybm - Developer <br>
Paulo Vitor Leite Tobias - pvitor7 - Developer <br>
