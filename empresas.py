from funcionarios import menu_funcionarios_empresa
from servicos_empresa import menu_servicos_empresa
from banco import conectar


def listar_empresas(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT ID, Nome FROM Empresa")
  empresas = cursor.fetchall()
  cursor.close()

  if empresas:
    print("\nLista de Empresas:")
    for empresa in empresas:
      print(f"{empresa[0]}. {empresa[1]}")
    return empresas
  else:
    print("\nNenhuma empresa cadastrada.")
    return None


def ler_empresa(conn, id_empresa):
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Empresa WHERE ID = %s', (id_empresa, ))
  empresa = cursor.fetchone()
  cursor.close()

  if empresa:
    print("\nDetalhes da Empresa:")
    print(f"ID: {empresa[0]}")
    print(f"Nome: {empresa[1]}")
    print(f"CNPJ: {empresa[2]}")
    print(f"Email: {empresa[3]}")
    print(f"Endereço: {empresa[4]}")

  else:
    print("\nEmpresa não encontrada.")


def criar_empresa(conn, nome, cnpj, email, endereco, senha):
  cursor = conn.cursor()
  cursor.execute(
      '''
      INSERT INTO Empresa (Nome, CNPJ, Email, Endereco, Senha)
      VALUES (%s, %s, %s, %s, %s)
      ''', (nome, cnpj, email, endereco, senha))
  conn.commit()
  cursor.close()
  print("\nEmpresa criada com sucesso.")


def atualizar_empresa(conn, id_empresa):
  cursor = conn.cursor()
  nome = input("Novo Nome da Empresa: ")
  cnpj = input("Novo CNPJ da Empresa: ")
  email = input("Novo Email da Empresa: ")
  endereco = input("Novo Endereço da Empresa: ")
  senha = input("Nova Senha da Empresa: ")

  cursor.execute(
      '''
      UPDATE Empresa
      SET Nome=%s, CNPJ=%s, Email=%s, Endereco=%s, Senha=%s
      WHERE ID=%s
  ''', (nome, cnpj, email, endereco, senha, id_empresa))

  conn.commit()
  cursor.close()
  print("\nEmpresa atualizada com sucesso.")


def deletar_empresa(conn, id_empresa):
  cursor = conn.cursor()
  # Verificar se a empresa existe antes de deletar
  cursor.execute("SELECT * FROM Empresa WHERE ID=%s", (id_empresa, ))
  empresa = cursor.fetchone()

  if empresa:
    confirmacao = input(
        f"Tem certeza que deseja deletar a empresa '{empresa[1]}'? (S/N): ")

    if confirmacao.lower() == 's':
      cursor.execute("DELETE FROM Empresa WHERE ID=%s", (id_empresa, ))
      conn.commit()
      cursor.close()
      print("\nEmpresa deletada com sucesso.")
    else:
      print("\nOperação de exclusão cancelada.")
  else:
    print("\nEmpresa não encontrada.")
    cursor.close()


def gerenciar_empresa(conn, id_empresa):
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Empresa WHERE ID=%s", (id_empresa, ))
  empresa = cursor.fetchone()

  while True:
    print(f"\n------ Gerenciar Empresa '{empresa[1]}' ------")
    print("1. Ler Empresa")
    print("2. Gerenciar Serviços")
    print("3. Gerenciar Funcionários")
    print("0. Voltar ao Menu de Empresa")
    escolha_empresa = input("Escolha a opção: ")

    if escolha_empresa == '1':  # ler empresa
      ler_empresa(conn, id_empresa)

    elif escolha_empresa == '2':  # gerenciar servicos da empresa
      menu_servicos_empresa(conn, empresa, id_empresa)

    elif escolha_empresa == '3':  # gerenciar funcionarios da empresa
      menu_funcionarios_empresa(conn, empresa, id_empresa)

    elif escolha_empresa == '0':
      cursor.close()
      break
    else:
      print("\nOpção inválida. Tente novamente.")


def menu_empresas(conn):
  while True:
    print("\n------ Menu Empresa ------")
    print("1. Criar Empresa")
    print("2. Atualizar Dados da Empresa")
    print("3. Gerenciar Empresa")
    print("4. Deletar Empresa")
    print("0. Voltar ao Menu Inicial")

    escolha_empresa = input("Escolha a opção: ")

    if escolha_empresa == '1':  # criar
      nome = input("\nNome da Empresa: ")
      cnpj = input("CNPJ da Empresa: ")
      email = input("Email da Empresa: ")
      endereco = input("Endereço da Empresa: ")
      senha = input("Senha da Empresa: ")
      criar_empresa(conn, nome, cnpj, email, endereco, senha)

    elif escolha_empresa == '2':  # atualizar
      empresas = listar_empresas(conn)
      if empresas:
        id_empresa = input("\nDigite o ID da Empresa para atualizar: ")
        atualizar_empresa(conn, id_empresa)

    elif escolha_empresa == '3':  # gerenciar
      empresas = listar_empresas(conn)
      if empresas:
        id_empresa = input("\nDigite o ID da Empresa para gerenciar: ")
        gerenciar_empresa(conn, id_empresa)

    elif escolha_empresa == '4':  # deletar
      empresas = listar_empresas(conn)
      if empresas:
        id_empresa = input("\nDigite o ID da Empresa para deletar: ")
        deletar_empresa(conn, id_empresa)

    elif escolha_empresa == '0':  # volta ao menu inicial
      break

    else:
      print("\nOpção inválida. Tente novamente.")
