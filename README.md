# Aula 09 - Docker Compose

O repositório contém dois cenários independentes para praticar Docker Compose.

## Cenário 1: aplicação Python

Construa e inicie os containers:

```powershell
cd cenario1
docker compose up --build -d
```

O ambiente inclui a calculadora financeira e um container vizinho para testar
a conectividade na rede do Compose:

```powershell
docker compose exec servico-vizinho ping -c 4 calculadora-app
```

Para encerrar:

```powershell
docker compose down
```

## Cenário 2: WordPress e MariaDB

Inicie a aplicação:

```powershell
cd cenario2
docker compose up -d
```

Acesse o WordPress em <http://localhost:8080>. Para verificar os containers:

```powershell
docker compose ps
```

Para encerrar e também remover os dados persistidos do banco:

```powershell
docker compose down -v
```
