CREATE table if not EXISTS produtos_da_empresa (
	id_produto INT  AUTO_INCREMENT,
  	nome_produto VARCHAR(100),
  	produtos_comprados_no_dia INT, 
  	PRIMARY KEY (id_produto)
);

INSERT INTO produtos_da_empresa(id_produto, nome_produto, produtos_comprados_no_dia)
VALUES
(default, 'Telefone', '500');


CREATE PROCEDURE consultar_quantidade_de_produtos()
BEGIN
	SELECT produtos_comprados_no_dia from produtos_da_empresa;
END; 


call consultar_quantidade_de_produtos();