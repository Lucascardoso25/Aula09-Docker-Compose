# Aula 09 - Docker Compose

O repositório contém dois cenários independentes para praticar Docker Compose.

## Cenário 1: Aplicação Python

Construa e inicie os containers:

```powershell
cd cenario1

docker compose up --build -d
```

O ambiente inclui a calculadora financeira e um container vizinho para testar a conectividade na rede do Compose:

```powershell
docker compose exec servico-vizinho ping -c 4 calculadora-app
```

Para encerrar os containers:

```powershell
docker compose down
```

## Cenário 2: WordPress e MariaDB

Inicie a aplicação:

```powershell
cd cenario2

docker compose up -d
```

### Acessando o WordPress

A aplicação WordPress está configurada para utilizar a porta **8081**, evitando conflitos com serviços locais, como Apache e MySQL do XAMPP.

Acesse pelo navegador:

- **Endereço principal:** http://localhost:8081
- **Endereço alternativo:** http://127.0.0.1:8081

Se o endereço `http://localhost:8081` não carregar, tente acessar diretamente pelo IP de loopback:

👉 http://127.0.0.1:8081

Caso esteja utilizando uma configuração anterior, o endereço `http://localhost:8080` também pode ser testado, desde que a porta esteja configurada corretamente no Docker Compose.

### Verificando os containers

Para verificar o estado dos containers:

```powershell
docker compose ps
```

### Encerrando a aplicação

Para encerrar os containers e remover os dados persistidos do banco de dados:

```powershell
docker compose down -v
```

**Atenção:** o parâmetro `-v` remove os volumes associados ao projeto, incluindo os dados persistidos do MariaDB. Utilize-o somente se desejar apagar esses dados.

## Resolução de Problemas de Acesso (XAMPP / Localhost)

- **Porta do serviço:** a porta externa do WordPress foi configurada para `8081` para evitar conflitos com serviços locais, como Apache e MySQL do XAMPP.
- **Endereço de acesso:** se `http://localhost:8081` ou `http://localhost:8080` não carregar devido ao cache do navegador ou a possíveis conflitos com o XAMPP, tente acessar diretamente pelo IP de loopback.
- **Acesso recomendado:** http://127.0.0.1:8081

Se o problema persistir, verifique se os containers estão em execução com `docker compose ps` e confirme se a porta `8081` está mapeada corretamente no arquivo `docker-compose.yml` do cenário 2.
