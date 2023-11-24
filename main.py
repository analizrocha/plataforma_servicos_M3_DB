from banco import conectar, cria_tabelas
from empresas import menu_empresas
from servicos import menu_servicos

# Conectar ao banco de dados
conn = conectar()
cria_tabelas(conn)

while True:
  print("\n------ Menu Inicial ------")
  print("1. Empresa")
  print("2. Serviços")
  print("0. Sair")

  escolha_inicial = input("Escolha a opção: ")

  if escolha_inicial == '1':
    menu_empresas(conn)

  elif escolha_inicial == '2':
    menu_servicos(conn)

  elif escolha_inicial == '0':  # termina programa
    print("Saindo do programa.")
    break

  else:
    print("Opção inválida. Tente novamente.")

# Fechar a conexão ao final do programa
conn.close()
