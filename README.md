# FastAPI Authentication & Authorization API

## Sumário

1. [Objetivo](#objetivo)
2. [Requisitos](#requisitos)
3. [Instalação](#instalação)
4. [Acessando as Rotas](#acessando-as-rotas)
5. [Executando os Testes](#executando-os-testes)

## Objetivo

Esta API foi desenvolvida para demonstrar um sistema de autenticação e autorização baseado em **JWT (JSON Web Tokens)**. Ela inclui endpoints protegidos que apenas usuários com permissões específicas podem acessar.

- **/token**: Gera um token JWT ao receber credenciais válidas.
- **/user**: Endereço acessível apenas por usuários com o papel **user**.
- **/admin**: Endereço acessível apenas por usuários com o papel **admin**.

Além disso, utiliza um banco de dados para gerenciar os usuários, salvando-os de forma persistente e utilizando consultas para autenticação.

## Requisitos

Certifique-se de ter o seguinte software instalado em sua máquina:

- **Python 3.9+**
- **SQLite3** (ou outro banco de dados caso queira modificar)
- **Git**

## Instalação

Clone o repositório

```bash
git clone https://github.com/josejonatasoliveira/api_jwt_authentication
```

Entre no projeto executando o seguinte comando no terminal.

```bash
cd api_jwt_authentication
```

Após isso crie um ambiente virtual para realizar as instalações das dependencias.
```bash
python -m venv .venv
```

Ative o ambiente executando o seguinte comando.
```bash
source .venv/bin/activate
```

Instale as dependencias do projeto.

```bash
pip install -r requirements-test.txt
```

Após isso é necessário realizar a migração e criação da base de dados.
Para isso deve-se executar o seguinte comando.

```bash
alembic upgrade head
```

Isso fará com que a tabela user seja criada no banco de dados.

E, por fim, para rodar o projeto execute o seguinte comando.

```bash
uvicorn app.main:app --reload --port 8005
```

## Acessando as Rotas

O FastAPI fornece uma interface de documentação interativa via Swagger.

Após iniciar a API, acesse a documentação interativa do Swagger:

- http://localhost:8005/docs

**Testando Endpoints**

1. **Obter um Token**
No Swagger, vá até o endpoint POST /token e insira as credenciais dos usuários fictícios:

**User**:
- username: user
- password: L0XuwPOdS5U

**Admin**:
- username: admin
- password: JKSipm0YH

Ao enviar a requisição, um token JWT será retornado.

2. **Acessar rotas protegidas**

Com o token obtido, vá para os endpoints /user ou /admin, clique em "Authorize" no Swagger, insira o token no formato Bearer <token> e teste os endpoints protegidos.

- `/user` é acessível somente para o usuário com papel user.
- `/admin` é acessível somente para o usuário com papel admin.

## Executando os Testes

1. **Como rodar os testes**

A API foi projetada com testes que utilizam pytest e httpx. Para rodar os testes, execute o seguinte comando:

```bash
pytest
```
