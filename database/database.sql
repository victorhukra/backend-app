CREATE DATABASE IF NOT EXISTS loja CHARACTER SET utf8mb4;
USE loja;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nome, email) VALUES
('Ana', 'ana@email.com'),
('Bruno', 'bruno@email.com');

INSERT INTO produtos (nome, descricao, preco, usuario_id) VALUES
('Mouse Gamer', 'Mouse com 6 botoes', 150.00, 1),
('Teclado Mecanico', 'Switch azul', 250.00, 1),
('Headset Gamer', 'Com microfone', 200.00, 2);

select * from produtos