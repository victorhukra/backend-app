USE loja;

ALTER TABLE usuarios
ADD COLUMN senha_hash VARCHAR(255) NULL;
