# FastAPI Taskboard Challenge

## Rotas Disponíveis

### Tarefas (Tasks)

- `GET /tasks/`: Retorna todas as tarefas cadastradas.
- `POST /tasks/`: Cria uma nova tarefa.
- `GET /tasks/{task_id}`: Retorna uma tarefa específica pelo ID.
- `PUT /tasks/{task_id}`: Atualiza uma tarefa existente pelo ID.
- `DELETE /tasks/{task_id}`: Exclui uma tarefa existente pelo ID.

### Status

- `GET /status/`: Retorna todos os status cadastrados.
- `POST /status/`: Cria um novo status.
- `GET /status/{status_id}`: Retorna um status específico pelo ID.
- `PUT /status/{status_id}`: Atualiza um status existente pelo ID.
- `DELETE /status/{status_id}`: Exclui um status existente pelo ID.

### Ícones (Icones)

- `GET /icones/`: Retorna todos os ícones cadastrados.
- `POST /icones/`: Cria um novo ícone.
- `GET /icones/{icone_id}`: Retorna um ícone específico pelo ID.
- `PUT /icones/{icone_id}`: Atualiza um ícone existente pelo ID.
- `DELETE /icones/{icone_id}`: Exclui um ícone existente pelo ID.
