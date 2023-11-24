def listar_funcionarios(conn, id_empresa):
  cursor = conn.cursor()
  cursor.execute("SELECT ID, Nome FROM Funcionarios WHERE ID_Empresa = %s",
                 (id_empresa, ))
  funcionarios = cursor.fetchall()
  cursor.close()

  if funcionarios:
    print("\nLista de Funcionários:")
    for funcionario in funcionarios:
      print(f"{funcionario[0]}. {funcionario[1]}")
    return funcionarios
  else:
    print("\nNenhum funcionário cadastrado.")
    return None


def criar_funcionario(conn, nome, id_empresa):
  cursor = conn.cursor()
  cursor.execute(
      '''
        INSERT INTO Funcionarios (Nome, ID_Empresa)
        VALUES (%s, %s)
        ''', (nome, id_empresa))
  conn.commit()
  cursor.close()
  print("\nFuncionário criado com sucesso.")

def atualizar_funcionario(conn, id_funcionario):
  nome = input("\nNovo Nome do Funcionário: ")

  cursor = conn.cursor()
  cursor.execute(
      '''
        UPDATE Funcionarios
        SET Nome=%s
        WHERE ID=%s
    ''', (nome, id_funcionario))

  conn.commit()
  cursor.close()

  print("\nFuncionário atualizado com sucesso.")


def deletar_funcionario(conn, id_funcionario):
  # Verificar se o funcionário existe antes de deletar
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Funcionarios WHERE ID=%s", (id_funcionario, ))
  funcionario = cursor.fetchone()

  if funcionario:
    confirmacao = input(
        f"\nTem certeza que deseja deletar o funcionário '{funcionario[1]}'? (S/N): "
    )

    if confirmacao.lower() == 's':
      cursor.execute("DELETE FROM Funcionarios WHERE ID=%s", (id_funcionario, ))
      conn.commit()
      print("\nFuncionário deletado com sucesso.")
    else:
      print("\nOperação de exclusão cancelada.")
  else:
    print("\nFuncionário não encontrado.")

  cursor.close()


def menu_funcionarios_empresa(conn, empresa, id_empresa):
  while True:
    print(f"\n------ Gerenciar Funcionários da Empresa '{empresa[1]}' ------")
    print("1. Listar Funcionários da Empresa")
    print("2. Atualizar Funcionário pelo ID")
    print("3. Adicionar Novo Funcionário")
    print("4. Remover Funcionário")
    print("0. Voltar ao Menu de Gerenciar Empresa")
    escolha_funcionarios = input("Escolha a opção: ")

    if escolha_funcionarios == '1':
      listar_funcionarios(conn, id_empresa)

    elif escolha_funcionarios == '2':
      funcionarios = listar_funcionarios(conn, id_empresa)

      if funcionarios:
        id_funcionario = input(
            "\nDigite o ID do Funcionário que deseja atualizar: ")
        atualizar_funcionario(conn, id_funcionario)

    elif escolha_funcionarios == '3':
      nome = input("\nDigite o nome do novo Funcionário: ")
      criar_funcionario(conn, nome, id_empresa)

    elif escolha_funcionarios == '4':
      funcionarios = listar_funcionarios(conn, id_empresa)

      if funcionarios:
        id_funcionario = input("\nDigite o ID do Funcionário que deseja remover: ")
        deletar_funcionario(conn, id_funcionario)

    elif escolha_funcionarios == '0':
      break

    else:
      print("\nOpção inválida. Tente novamente.")
