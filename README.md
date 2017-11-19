# Seu Direito

Projeto que permite a comunicação entre empresas e advogados. As empresas cadastradas podem solicitar ordens de serviço e os advogados cadastrados no sistema podem publicar o preço avalida a cada ordem.

## Inicializando

O projeto deve ser inicializado com os seguintes passos:

1. Iniciar a máquina virtual - `docker-machine create -d virtualbox dev;` 
2. No diretório SeuDireito, iniciar o container - `docker-compose up`
3. Criar as migrações: `docker-compose run web /usr/local/bin/python manage.py migrate `
4. Encontrar o ip da máquina com: `docker-machine ip dev`
5. No browser, rodar na porta 8000.

### Pré-requisitos

Os únicos requisitos do projeto são o docker, docker-compose e o docker-machine. As maneiras de instalar são diferentes para cada sistema operacional.

Todos os pré-requisitos além destes estão no arquivo 'requirements.txt'. Estes requisitos são instalados com a inicialização do docker. Pelo Dockerfile:
```
 FROM python:3.6
 RUN apt-get update \
    && apt-get install -y postgresql-client-9.4 \
    && rm -rf /var/lib/apt/lists/
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 
```
 

### Estrutura

A database utilizada é PostgreSQL, que é instalada pelo requirements.txt. Nesta database estão as tabelas de Advogados e Empresas, que extendem o usuário normal do Django para autenticação na página de login.

Existem dados para cada ordem de serviço no model OrdemServico. E a relação entre os preços solicitados pelos advogados e a ordem, no model Preco.

O projeto foi feito com o Django Rest Framework no backend e AngularJS no front-end.

### Utilização do Programa

O usuário inicialmente pode se cadastrar como Advogado ou como Empresa. Ao se cadastrar cada um é redirecionado para uma página diferente.

Os Advogados podem ver a listagem das ordens e o status de cada ordem. Só podem definir um preço para uma ordem se ela estiver com o status 'Criada'. Ao definir o preço estas informações são direcionadas para a Empresa que cadastrou a ordem, que pode avaliar entre todas as propostas, e definir como 'Delegada' aquela que achar mais conveniente.
