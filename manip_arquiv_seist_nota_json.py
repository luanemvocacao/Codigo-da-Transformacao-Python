import json
import os

# Define o nome do arquivo JSON.
nome_arquivo_json = "clientes.json"

# Função para adicionar um novo cliente.
def adicionar_cliente():
    # Carrega os dados existentes do arquivo. Se o arquivo não existir, começa com um dicionário vazio.
    clientes = {}
    if os.path.exists(nome_arquivo_json):
        with open(nome_arquivo_json, 'r') as arquivo_json:
            clientes = json.load(arquivo_json)

    # Pede as informações do novo cliente ao usuário.
    print("\n--- Adicionar Novo Cliente ---")
    nome = input("Digite o nome do cliente: ")
    
    # Verifica se o cliente já existe para evitar duplicados.
    if nome in clientes:
        print(f"❌ Erro: O cliente '{nome}' já existe na base de dados.")
        return

    cliente_id = input("Digite o ID do cliente: ")
    cidade = input("Digite a cidade do cliente: ")

    # Adiciona o novo cliente ao dicionário.
    clientes[nome] = {
        "id": cliente_id,
        "cidade": cidade
    }
    
    # Salva o dicionário completo e atualizado de volta no arquivo.
    with open(nome_arquivo_json, 'w') as arquivo_json:
        json.dump(clientes, arquivo_json, indent=4)
        
    print(f"✅ Cliente '{nome}' adicionado e salvo com sucesso!")


# Função para visualizar todos os clientes.
def visualizar_clientes():
    # Verifica se o arquivo JSON existe.
    if not os.path.exists(nome_arquivo_json):
        print("📝 O arquivo de clientes ainda não existe.")
        return

    # Carrega os dados do arquivo.
    with open(nome_arquivo_json, 'r') as arquivo_json:
        clientes = json.load(arquivo_json)
    
    if not clientes:
        print("📝 A lista de clientes está vazia.")
        return

    print("\n--- Lista de Clientes ---")
    # Percorre o dicionário para mostrar os detalhes de cada cliente.
    for nome, detalhes in clientes.items():
        print(f"Nome: {nome}")
        print(f"  ID: {detalhes['id']}")
        print(f"  Cidade: {detalhes['cidade']}")
        print("-------------------------")


# ======================================================================
# 🔄 Passo 3: O Loop do Menu Principal
# O menu principal do nosso programa.
while True:
    print("\n--- Menu do Gerenciador de Clientes ---")
    print("1. Adicionar cliente")
    print("2. Visualizar clientes")
    print("3. Sair")
    
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        adicionar_cliente()
    elif escolha == '2':
        visualizar_clientes()
    elif escolha == '3':
        print("👋 Saindo do programa. Até mais!")
        break
    else:
        print("🚫 Opção inválida. Por favor, digite 1, 2 ou 3.")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================