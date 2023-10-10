CREATE table if not EXISTS aluno(
	Pnome VARCHAR,
  	Unome VARCHAR,
  	matricula INT PRIMARY KEY UNIQUE,
  	serie CHAR(6),
  	disciplina VARCHAR,
  	nota FLOAT
);

drop table alunos;

INSERT INTO aluno(Pnome, Unome, matricula, serie, disciplina, nota)
VALUES 
('Vitória', 'Claudiano', '5542', '2º ano', 'Matemática', '7.0'),
('Luiz', 'silva', '6215', '1º ano', 'Português', '8.0'),
('André', 'Carvalho', '4521', '3º ano', 'Matemática', '9.5'),
('Alan', 'Vilela', '3285', '1º ano', 'História', '8.0'),
('Figueiredo', 'Santos', '4598', '2º ano', 'Geografia', '9.0');

SELECT * from aluno WHERE nota > '7.0';
SELECT * from aluno where nota >= '8.0' and serie = '1º ano';
SELECT Unome, nota from aluno;

CREATE table if not EXISTS professor(
	Pnome VARCHAR,
  	Unome VARCHAR
);

INSERT INTO professor(Pnome, Unome)
VALUES 
('Vitoriano', 'Silva'),
('Luiza', 'Tchaikovsky'),
('Ander', 'lemos'),
('Alana', 'Vilmar'),
('Fiora', 'Santana');

select * from professor;

CREATE table if not EXISTS aluno(
	Pnome VARCHAR,
  	Unome VARCHAR
);

INSERT into aluno(Pnome, Unome)
VALUES
('Vitória', 'Claudiano'),
('Luiz', 'silva'),
('André', 'Carvalho'),
('Alan', 'Vilela'),
('Figueiredo', 'Santos');

SELECT * from aluno;


