
# Northwind DataBase - Python 3.11.3

Uma breve aplicação desenvolvida em Pyhton que consome um banco de dados configurado usando o docker compose, e um arquivo csv em memória local, salvando essas informações em formato json no diretório do projeto, em seguida persistindo esses dados em um banco também utilizando docker compose. 




## Instalação e configurações de ambiente

Para executar o projeto, é necessário ter instalado uma versão igual ou superior ao [Python 3.11.3](https://www.python.org/downloads/ ), e o [Docker]( https://docs.docker.com/compose/install/). Após obter a versão correta, faça o clone do repositório para sua máquina.

```bash
git clone https://github.com/thiagoaure/application-northwinddb-python
```


## Run

Para executar o projeto sem nenhum problema de conexão, execute os dois containers docker onde estão a imagem do PostgreSQL (banco de origem) e MongoDB (banco escolhido como destino). Execute no diretório do projeto:

```
docker-compose -f .\docker-compose.yml up
```
```
docker-compose -f .\docker-compose-mongodb.yml up
```

Após a execução dos comandos, aguarda um tempo e verifiue nos logs se o banco postgre foi populado com as informações do data\northwind.sql, depois observe se os  ontainers estão em execução:

```
docker ps 
```

Se estiver os dois em execução, está pronto para processar os dados na aplicação na qual se divide em 4 partes:

- Ler os dados do arquivo em data\order_details.csv e salvar no diretório data\csv\order_details\ em formato JSON.
- Ler os dados do banco PostgreSQL e salvar do diretório data\postgres em formato JSON.
- Inserir os dados que estão salvos no diretório local no banco nosql MongoDB.
- Ler todos os dados salvos no MongoDB e salvar na memória local em formato JSON.

OBS: Todos os dados são armazenados separadamente por tabela e data de execução da tarefa. Sendo assim, ao executar a tarefa de Inserir os dados no MongoDB, fica opcional passar a data escolhida para obter os dados processados naquele dia, caso contário será levado em consideração a data do dia corrido.

Por fim, para executar a aplicação e ter acesso ao menu de opções, recomendo ir ao terminal do diretório do projeto, e executar o arquivo main.py:

```
py python/main.py
```
## Referência

Todos projeto é baseado no desafio proposto pela Indicium

 - [Desafio de Engenharia de Dados](https://github.com/techindicium/code-challenge)

