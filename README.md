# TaskTracker - Fase 3: Conteinerização e Orquestração

Aplicação CLI em Python para gerenciamento de tarefas, empacotada e orquestrada com Docker e Docker Compose.

* [Acessar Planejamento do Projeto (DOCS)](https://docs.google.com/document/d/1nu18XMsco4xrMxYKYSVCJDb98IfJz3JbE-0dh4BNk0U/edit?usp=sharing)

## Como Executar a Aplicação

### 1. Construir a imagem Docker
```bash
docker build -t tasktracker .
```

### 2. Rodar o container em modo interativo
```bash
docker run -it tasktracker
```

### 3. Rodar via Docker Compose (Recomendado)
```bash
docker compose run tasktracker-app
```