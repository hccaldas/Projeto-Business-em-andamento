Dashboard de Análise de Vendas em Tempo Real

📌 Sobre o Projeto

Este projeto tem como objetivo criar um dashboard de análise de vendas em tempo real, acessível tanto para administradores quanto para clientes, com login e permissões configuráveis.

O projeto inclui:

Backend em Python (FastAPI)
Frontend em Streamlit
Banco de Dados MySQL
Visualização de dados com Power BI
Atualização de dados em tempo real via API e periodicamente a cada dia

🛠️ Ferramentas e Tecnologias Utilizadas

Linguagens e Frameworks:
Python (Linguagem principal)
FastAPI (Framework para API)
Streamlit (Frontend interativo)
MySQL (Banco de dados relacional)
Power BI (Visualização de dados)

Bibliotecas Python:

uvicorn (Servidor ASGI para rodar o FastAPI)
fastapi (Criação de APIs)
mysql-connector-python (Conexão com MySQL)
pyjwt (Autenticação JWT para login)
hashlib (Criptografia de senhas SHA-256)
datetime (Manipulação de datas)

Softwares e Plataformas:

MySQL Server (Banco de dados local ou remoto)
DBeaver ou MySQL Workbench (Gerenciamento do banco)
Postman ou FastAPI Docs (Testes da API)
VS Code ou PyCharm (Editor de código)
Power BI (Criação de dashboards)

ESTRUTURA DO PROJETO

📂 dashboard-vendas
│-- 📂 routes
│   │-- usuarios.py  # Rota para CRUD de usuários
│   │-- login.py     # Rota para autenticação e login JWT
│-- 📂 models
│   │-- usuario.py   # Modelo de dados para usuários
│-- 📂 database
│   │-- database.py  # Conexão com o MySQL
│-- auth.py         # Gera tokens JWT
│-- main.py         # Arquivo principal da API FastAPI
│-- README.md       # Documentação do projeto


 ##############################O Que Já Foi Feito#############################

🔹 1. Configuração do Banco de Dados (MySQL)

Criamos um banco de dados chamado dashboard_vendas e a tabela usuarios:

CREATE DATABASE dashboard_vendas;
USE dashboard_vendas;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    tipo ENUM('admin', 'cliente') NOT NULL
);

🔹 2. Configuração do Backend (FastAPI)

Criamos o main.py e iniciamos o servidor com uvicorn.

uvicorn main:app --reload

🔹 3. Rota de Cadastro de Usuários (POST /usuarios/)

Criamos um endpoint para cadastrar novos usuários com senha criptografada (SHA-256).

🔹 4. Rota de Login (POST /login/)

Criamos um endpoint para autenticação de usuários, gerando um token JWT para acesso.


em processo %%%%%%


################################O que falta fazer#####################################


✅ Revisar o Backend do Zero para corrigir erros e validar a estrutura.
✅ Criar rotas protegidas para que apenas usuários autenticados possam acessar dados.
✅ Criar a API de Vendas para armazenar e consultar vendas no banco.
✅ Implementar o Frontend (Streamlit) para exibir os dados em tempo real.
✅ Integrar com o Power BI para visualização dos dados.

