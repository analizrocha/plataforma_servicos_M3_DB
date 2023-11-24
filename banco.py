import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
  host = os.environ.get("HOST")
  port = os.environ.get("PORT", 3306)
  user = os.environ.get("USER")
  password = os.environ.get("PASSWORD")
  database = os.environ.get("DATABASE")

  conn = mysql.connector.connect(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 database=database)

  return conn
  
def cria_tabelas(conn):
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS plataforma_servicos")
    cursor.execute("USE plataforma_servicos")

    # Criação da tabela Empresa
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Empresa (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(255) NOT NULL,
            CNPJ VARCHAR(18) NOT NULL,
            Email VARCHAR(255) NOT NULL,
            Endereco VARCHAR(255) NOT NULL,
            Senha VARCHAR(255) NOT NULL
        )
    """)

    # Criação da tabela Funcionarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Funcionarios (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(255) NOT NULL,
            ID_Empresa INT NOT NULL,
            FOREIGN KEY (ID_Empresa) REFERENCES Empresa(ID)
        )
    """)

    # Criação da tabela Servicos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Servicos (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(255) NOT NULL,
            Descricao TEXT,
            Preco DECIMAL(10, 2) NOT NULL
        )
    """)

    # Criação da tabela Servicos_Empresa
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Servicos_Empresa (
            ID_Empresa INT NOT NULL,
            ID_Servico INT NOT NULL,
            PRIMARY KEY (ID_Empresa, ID_Servico),
            FOREIGN KEY (ID_Empresa) REFERENCES Empresa(ID),
            FOREIGN KEY (ID_Servico) REFERENCES Servicos(ID)
        )
    """)

    conn.commit()
    cursor.close()
