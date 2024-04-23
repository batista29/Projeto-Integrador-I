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

SELECT * FROM Estoque;

INSERT into Estoque values (6,'Caderno','Ponte Preta',10,30,20,20,29.99);

UPDATE Estoque SET custo_fixo = 250 WHERE id_prod = 36;

DELETE FROM Estoque WHERE id_prod = 36;

INSERT into Estoque values (3,'lápis','chines',0.21,10,5,18,0);

COMMIT;