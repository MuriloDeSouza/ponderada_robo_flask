# Projeto Robô CRUD com Flask e HTMX

Este projeto é meio que um sistema de CRUD (Create, Read, Update, Delete) desenvolvido com a API Flask no backend e HTMX no frontend. Ele oferece uma interface web para interagir com um robô, fornecendo coordenadas de posição, permitindo o retorno à posição de origem (home), coordenadas da posição atual, adicionar as posições que eu quero que ele se moviemnto em x, y, z e a rotação r e controlando a abertura e o fechamento da garra do robô.

## Funcionalidades

- **Controle de Posição**: Permite fornecer coordenadas de posição (x, y, z, r) para o robô.
- **Home**: Botão para retornar o robô à posição de origem.
- **Controle da Garra**: Permite abrir e fechar a garra do robô.

## Pagina de Logs
A página de logs é uma tabela HTML que exibe os dados enviados pelo servidor em tempo real. Cada linha representa um evento registrado no sistema (os pontos que ele visitou)

- **Logs**: Registra as localizações visitadas pelo robô, armazenadas em um banco de dados TinyDB.

## Motivação

Este projeto foi desenvolvido como uma solução para facilitar o controle e monitoramento de um robô. A utilização do Flask no backend oferece uma estrutura robusta e flexível para lidar com as operações de CRUD, enquanto o HTMX no frontend proporciona uma interação dinâmica e responsiva com o usuário, sem a necessidade de recarregar a página.

## Tecnologias usadas

O Projeto utlizou:

- **FLASK**: API para ajudar no BACKEND
- **HTMX**: Biblioteca JavaScript para ajudar na criação da interface FRONTEND
- **Python**: Linguagem de programação utilizada para construir o BACKEND
- **Bootstrap e Bootstrap icons**:  Framework para desenvolvimento de componentes de interface responsivos e os ícones para deixar a interface bonita. 

## Instalação

1. Clone este repositório:
```bash
https://github.com/MuriloDeSouza/ponderada_robo_flask
```

2. Entre no diretório do projeto:

```bash
cd ponderada_robo_flask
```

3. Instale as dependências utilizando pip:

```bash
pip install -r requirements.txt
```

## Para o projeto funcionar

Garanta que você esteja no local certo para rodar:
```bash
ponderada_robo_flask\src\backend
```

Depois que estiver nesse diretório, você pode rodar o projeto com o comando:

```bash
python rotas.py
```


