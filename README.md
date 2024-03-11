# TecnisysPost
Plataforma desenvolvida pela TecniSys para gereciamento e apoio de banco de dados usando o PostGres

---
## Conectando um cluster(onde as instâncias dos bancos de dados ficam)

  - Mudando para o usuário postgres
    - `su - postgres`
  - Conectando ao terminal postgres(entrando na instância)
    - `psql`
    - `\c` verifica o usuário conectado e o banco
    - Se não informar qualo banco de dados e o usuário a conectar ele pega pelo usuário logado e o seu DB
  - Criando uma instância chamada curso
    - `create database curso;` sempre terminar com ponto e vìrgula
  - Para conectar a outra instância
    - `\c <nome da instância> `ou `\q` para sair e `psql <nome da instância>`
  - Criando um esquema
    - `create schema <nome>;` será criado dentro da instância
  - Criando uma tabela
    - `create table <nome do schema>.<nome da tabela>(<nome das colunas> <tipo>, ...);`
    - tipos de variáveis de colunas: `serial` começa por 0 e vai add números ,`primary key` escolhe uma coluna para ser a identificadora
  - Listar instâncias
    - `\l+`
  - Detalhar esquemas
    -`\dt <nome schema>.* ` * seleciona todas as tables
    -  List of relations        
     Schema  | Name  | Type  |  Owner    
        ---------+-------+-------+----------        
     prática | aluno | table | postgres

- Aluno : obj do tipo table que será convertida para número lá na lista do postgres

