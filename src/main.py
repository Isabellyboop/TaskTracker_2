def ler_titulo():
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: O título é obrigatório e não pode ser vazio.")

def ler_prioridade():
    opcoes_validas = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
    while True:
        entrada = input("Digite a prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in opcoes_validas:
            return opcoes_validas[entrada]
        print("Erro: Prioridade inválida. Digite apenas 'Alta', 'Média' ou 'Baixa'.")

def cadastrar_tarefa(lista_tarefas):
    print("\n--- CADASTRO DE TAREFA ---")
    
    titulo = ler_titulo()
    descricao = input("Digite a descrição da tarefa: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    lista_tarefas.append(tarefa)
    print("✓ Tarefa cadastrada com sucesso!")

def listar_tarefas(lista_tarefas):
    print("\n--- LISTA DE TAREFAS ---")
    
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for i, tarefa in enumerate(lista_tarefas, start=1):
        print(f"\nTarefa #{i}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao'] if tarefa['descricao'] else 'Não informada'}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data Limite: {tarefa['data_limite'] if tarefa['data_limite'] else 'Não informada'}")
        print(f"  Status:      {tarefa['status']}")
        print("-" * 30)

def main():
    tarefas = []
    
    while True:
        print("\n==============================")
        print("    GERENCIADOR DE TAREFAS    ")
        print("==============================")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        print("==============================")
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nSaindo da aplicação. Até logo!")
            break
        else:
            print("Erro: Opção inválida. Digite 1, 2 ou 3.")

if __name__ == "__main__":
    main()