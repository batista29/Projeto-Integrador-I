CREATE TABLE Estoque(
    id_prod INTEGER PRIMARY KEY NOT NULL,
    nome_prod VARCHAR2(255) NOT NULL,
    desc_prod VARCHAR2(255) NOT NULL,
    custo_prod NUMBER(10,2) NOT NULL,
    custo_fixo NUMBER(10,2) NOT NULL,
    comissao NUMBER (5,3) NOT NULL,
    imposto NUMBER (10,2) NOT NULL,
    rentabilidade NUMBER (6,3) NOT NULL
);

describe Estoque;

select * from Estoque;

INSERT into Estoque values (36,'geladeira','geladeira grande branca',5000,200,10,300,20);

UPDATE Estoque SET custo_fixo = 250 WHERE id_prod = 36;

DELETE FROM Estoque WHERE id_prod = 37;

INSERT into Estoque values (36,'geladeira','geladeira grande branca',36,15,12,5,20);

INSERT into Estoque values (37,'geladeira','geladeira pequena',1,1,1,1,0);

INSERT into Estoque values (3,'lápis','chines',0.21,10,5,18,0);