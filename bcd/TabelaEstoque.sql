CREATE TABLE Estoque(
    id_prod INTEGER PRIMARY KEY NOT NULL,
    nome_prod VARCHAR2 NOT NULL,
    desc_prod VARCHAR2 NOT NULL,
    custo_prod NUMBER(10,2) NOT NULL,
    custo_fixo NUMBER(10,2) NOT NULL,
    comissao NUMBER (5,3) NOT NULL,
    imposto NUMBER (10,2) NOT NULL,
    rentabilidade NUMBER (6,3) NOT NULL
);