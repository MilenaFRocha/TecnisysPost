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

  ## Objeto de sistemas
    - Grant dá acesso aos usuários ,não à roles, para conceder também o mesmo acesso
      - ![image](https://github.com/MilenaFRocha/TecnisysPost/assets/104432227/cfe81e6f-3f18-4fd6-bfe4-d104ad8653aa)
    - Para remover em forma cascata
      - ![image](https://github.com/MilenaFRocha/TecnisysPost/assets/104432227/27a03779-2704-4f33-8aa6-2236e9272a98)
    - RLS
      - ![image](https://github.com/MilenaFRocha/TecnisysPost/assets/104432227/77b8773b-4e51-4346-8e45-8cb0049c618f)
    - Boas Práticas
      - ![image](https://github.com/MilenaFRocha/TecnisysPost/assets/104432227/16d134f5-c159-45f0-93e4-d48276568006)

## Configurando o cluster para acesso
- Pelo pgsmart bem mais fácil , se fosse poderia editar o arquivo Pg_hba.conf por qualquer editor (vim,etc)
  - `pgsmart cluster config`
- Para ver entra no `psql ` e ` select * from pg_hba_file_rules;`

## GitHub do PostGres
- ![image](https://github.com/MilenaFRocha/TecnisysPost/assets/104432227/dbd49934-a104-4205-bf88-856e2b862478)

    

 

