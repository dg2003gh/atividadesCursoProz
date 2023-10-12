CREATE TABLE cliente(
	id_cliente SERIAL PRIMARY KEY, 
  	p_nome VARCHAR(40),
  	data_insercao DATE
);

INSERT into cliente(p_nome, data_insercao)
VALUES
('rodrigo', '2023-01-22'),
('ana', '2023-01-03'),
('carlos', '2022-02-02'),
('gregorio', '2023-10-12');


CREATE OR REPLACE FUNCTION consultar_clientes_dia()
	RETURNS SETOF cliente
	as $$
	BEGIN
      RETURN QUERY
      SELECT * from cliente WHERE data_insercao = CURRENT_DATE;
	END; $$ LANGUAGE PLPGSQL;

SELECT consultar_clientes_dia();