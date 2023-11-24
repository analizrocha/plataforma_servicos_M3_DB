CREATE DATABASE IF NOT EXISTS plataforma_servicos;

USE plataforma_servicos;

CREATE TABLE IF NOT EXISTS Empresa (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    CNPJ VARCHAR(18) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Endereco VARCHAR(255) NOT NULL,
    Senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Funcionarios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    ID_Empresa INT NOT NULL,
    FOREIGN KEY (ID_Empresa) REFERENCES Empresa(ID)
);
# Criação da tabela Servicos
CREATE TABLE IF NOT EXISTS Servicos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Descricao TEXT,
    Preco DECIMAL(10, 2) NOT NULL
)
# Criação da tabela Servicos_Empresa
CREATE TABLE IF NOT EXISTS Servicos_Empresa (
    ID_Empresa INT NOT NULL,
    ID_Servico INT NOT NULL,
    PRIMARY KEY (ID_Empresa, ID_Servico),
    FOREIGN KEY (ID_Empresa) REFERENCES Empresa(ID),
    FOREIGN KEY (ID_Servico) REFERENCES Servicos(ID)
)