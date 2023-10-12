create or REPLACE DATABASE loja;
use loja;

CREATE or REPLACE table produtos(
	id_produto INT AUTO_INCREMENT,
  	nome_produto VARCHAR(50),
  	preco_produto FLOAT,
  	PRIMARY KEY (id_produto)
);

CREATE or REPLACE table historico_compras(
	id_transacao INT AUTO_INCREMENT,	
  	fk_id_produto int,
  	data_compra DATE,
  	numero_produtos_comprados MEDIUMINT,
  	comprador_primeiro_nome varchar(50),
  	primary key(id_transacao),
  	FOREIGN key(fk_id_produto) REFERENCES produtos(id_produto)
);

INSERT INTO produtos(nome_produto, preco_produto)
VALUES 
('televisão', '1590.80'),
('smartphone', '2000'),
('geladeira', '3230.50'),
('sofá', '500.95');

SELECT * from produtos;

INSERT INTO historico_compras(data_compra, numero_produtos_comprados, comprador_primeiro_nome, fk_id_produto)
VALUES
('2023-05-01', '1', 'wiliam', '1'),
('2023-07-07', '2', 'ronaldo', '2'),
('2023-01-09', '1', 'alessandra','3'),
('2022-02-05', '5', 'almir', '4');

CREATE TRIGGER ao_adicionar_compra
 AFTER INSERT
 on historico_compras
 for EACH ROW
    BEGIN
		SELECT * FROM historico_compras;
    END;
