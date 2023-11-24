def listar_servicos(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT ID, Nome, Descricao FROM Servicos")
  servicos = cursor.fetchall()
  cursor.close()

  if servicos:
    print("\nLista de Serviços:")
    for servico in servicos:
      print(f"{servico[0]}. {servico[1]} - Descrição: {servico[2]}")
    return servicos
  else:
    print("\nNenhum serviço cadastrado.")
    return None

def pegar_servico_pelo_id(conn, id_servico):
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Servicos WHERE ID = %s', (id_servico, ))
  servico = cursor.fetchone()
  cursor.close()

  if servico:
    return servico
  else:
    return None

def criar_servico(conn, nome, descricao):
  cursor = conn.cursor()
  cursor.execute(
      '''
        INSERT INTO Servicos (Nome, Descricao)
        VALUES (%s, %s)
        ''', (nome, descricao))
  conn.commit()
  cursor.close()

  print("\nServiço criado com sucesso.")

def ler_servico(conn, id_servico):
  servico = pegar_servico_pelo_id(conn, id_servico)

  if servico:
    print("\nDetalhes do Serviço:")
    print(servico)
  else:
    print("\nServiço não encontrado.")


def atualizar_servico(conn, id_servico):
  nome = input("\nNovo Nome do Serviço: ")
  descricao = input("Nova Descrição do Serviço: ")

  cursor = conn.cursor()
  cursor.execute(
      '''
        UPDATE Servicos
        SET Nome=%s, Descricao=%s
        WHERE ID=%s
    ''', (nome, descricao, id_servico))

  conn.commit()
  cursor.close()

  print("\nServiço atualizado com sucesso.")


def deletar_servico(conn, id_servico):
  servico = pegar_servico_pelo_id(conn, id_servico)

  if servico:
    confirmacao = input(
        f"\nTodas as empresas que possuem esse serviço também o terão removido da sua base de serviços. Tem certeza que deseja deletar o serviço '{servico[1]}'? (S/N): "
    )

    if confirmacao.lower() == 's':
      cursor = conn.cursor()
      cursor.execute("DELETE FROM Servicos WHERE ID=%s", (id_servico, ))

      # Deletar todas as entradas relacionadas na tabela Servicos_empresa
      cursor.execute("DELETE FROM Servicos_empresa WHERE ID_Servico=%s",
                     (id_servico, ))

      conn.commit()
      cursor.close()

      print("\nServiço deletado com sucesso.")
    else:
      print("\nOperação de exclusão cancelada.")
  else:
    print("\nServiço não encontrado.")


def menu_servicos(conn):
  while True:
    print("\n------ Menu Serviços ------")
    print("1. Listar Serviços")
    print("2. Criar Serviço")
    print("3. Atualizar Serviço")
    print("4. Deletar Serviço")
    print("0. Voltar ao Menu Inicial")
    escolha_servico = input("Escolha a opção: ")

    if escolha_servico == '1':  # criar
      listar_servicos(conn)

    elif escolha_servico == '2':  # criar
      nome_servico = input("\nNome do Serviço: ")
      descricao_servico = input("Descrição do Serviço: ")

      criar_servico(conn, nome_servico, descricao_servico)

    elif escolha_servico == '3':  # atualizar
      servicos = listar_servicos(conn)
      if servicos:
        # Solicitar ID e exibir detalhes do serviço
        id_servico = input("\nDigite o ID do Serviço para atualizar: ")
        atualizar_servico(conn, id_servico)

    elif escolha_servico == '4':  # deletar
      servicos = listar_servicos(conn)
      if servicos:
        # Solicitar ID e exibir detalhes do serviço
        id_servico = input("\nDigite o ID do Serviço para deletar: ")
        deletar_servico(conn, id_servico)

    elif escolha_servico == '0':  # volta ao menu inicial
      break

    else:
      print("\nOpção inválida. Tente novamente.")
