CREATE DATABASE IF NOT EXISTS loja CHARACTER SET utf8mb4;

USE loja;

DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS usuarios;

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
('Bruno', 'bruno@email.com'),
('Carlos', 'carlos@email.com'),
('Daniel', 'daniel@email.com'),
('Eduarda', 'eduarda@email.com');

INSERT INTO produtos (nome, descricao, preco, usuario_id) VALUES
('Mouse Gamer', 'Mouse gamer com 6 botoes', 150.00, 1),
('Teclado Mecanico', 'Teclado mecanico com switch azul', 250.00, 1),
('Headset Gamer', 'Headset gamer com microfone', 200.00, 1),
('Mousepad Gamer', 'Mousepad grande para jogos', 80.00, 1),
('Webcam Full HD', 'Webcam com resolucao Full HD', 180.00, 1),

('Monitor 24 Polegadas', 'Monitor Full HD de 24 polegadas', 900.00, 2),
('Cadeira Gamer', 'Cadeira gamer com apoio de braco', 850.00, 2),
('Microfone USB', 'Microfone USB para computador', 300.00, 2),
('Suporte para Monitor', 'Suporte ajustavel para monitor', 120.00, 2),
('Controle Gamer', 'Controle USB para PC', 180.00, 2),

('Notebook', 'Notebook para estudos e trabalho', 3500.00, 3),
('SSD 1TB', 'SSD NVMe de 1TB', 450.00, 3),
('Memoria RAM 16GB', 'Memoria DDR4 16GB', 280.00, 3),
('HD Externo 2TB', 'HD externo USB de 2TB', 400.00, 3),
('Adaptador USB', 'Adaptador USB para computador', 60.00, 3),

('Placa de Video', 'Placa de video para jogos', 2500.00, 4),
('Fonte 650W', 'Fonte de alimentacao 650W', 350.00, 4),
('Gabinete Gamer', 'Gabinete com lateral em vidro', 400.00, 4),
('Cooler para CPU', 'Cooler para processador', 150.00, 4),
('Kit de Fans', 'Kit com 3 fans para gabinete', 100.00, 4),

('Processador Ryzen 5', 'Processador AMD Ryzen 5', 1000.00, 5),
('Placa Mae B550', 'Placa mae com socket AM4', 700.00, 5),
('Memoria RAM 32GB', 'Kit de memoria DDR4 32GB', 500.00, 5),
('SSD 500GB', 'SSD NVMe de 500GB', 250.00, 5),
('Roteador Wi-Fi', 'Roteador dual band', 300.00, 5);