USE loja;

-- Use somente em bancos antigos; database.sql já cria esta coluna em instalações novas.
ALTER TABLE usuarios
ADD COLUMN senha_hash VARCHAR(255) NULL;
