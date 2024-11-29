# ML-engineer-teste-celero
API de Gerenciamento de Itens
Descrição

Esta é uma API desenvolvida em Python utilizando o framework Flask. Ela permite gerenciar objetos com as seguintes operações:

<li>Listar itens
<li>Salvar (adicionar) um novo item
<li>Alterar um item existente
<li>Remover um item

A API foi projetada para ser clara, fácil de usar e implementada com boas práticas de desenvolvimento, incluindo testes com Pytest.

## Cada objeto possui os seguintes atributos:

<li>id (auto-incremental)
<li>nome (string)
<li>valor (float)
<li>data_criacao (ISO 8601 timestamp)
<li>eletronico (boolean)

## Para instalação usar:

```sh
bash setup.sh
```

## Rodando Localmente

```sh
    flask run
```
Acesse a aplicação localmente em: http://127.0.0.1:5000.

## Rotas API

### Listar objetos

<li>Método: GET

<li>URL: /api/v1/list_objects/

Exemplo de Resposta:

```json
[
  {
    "id": 1,
    "nome": "Notebook",
    "valor": 3000.0,
    "data_criacao": "2024-11-26T12:00:00",
    "eletronico": true
  },
  {
    "id": 2,
    "nome": "Caderno",
    "valor": 25.5,
    "data_criacao": "2024-11-27T10:30:00",
    "eletronico": false
  }
]
```

### Adicionar objeto

<li>Método: POST

<li>URL: /api/v1/add_object/

<li> Corpo da requisição json 

```json
{
  "nome": "Celular",
  "valor": 1500.0,
  "data_criacao": "2024-11-27T10:00:00",
  "eletronico": true
}
```

### Editar objeto

<li>Método: PUT

<li>URL: /api/v1/update_object/

<li> Corpo da requisição json 

```json
{
  "id": 1,
  "nome": "Alterado",
  "valor": 1500.0,
  "data_criacao": "2024-11-27T10:00:00",
  "eletronico": true
}
```

### Deletar objeto

<li>Método: DELETE

<li>URL: /api/v1/delete_object/

<li> Corpo da requisição json 

```json
{
  "id": 1
}
```

<li> Exemplo da Resposta:
```json
{
  "message": "Objeto com ID 1 foi deletado com sucesso."
}
```