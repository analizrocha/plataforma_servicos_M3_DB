from servicos import listar_servicos

def listar_servicos_empresa(conn, empresa, id_empresa):
  cursor = conn.cursor()
  cursor.execute("SELECT se.ID, s.Nome as NomeServico, se.Valor FROM Servicos_empresa se JOIN Empresa e ON se.ID_Empresa = e.ID JOIN Servicos s ON se.ID_Servico = s.ID WHERE e.id = %s", (id_empresa, ))
  servicos_empresa = cursor.fetchall()
  cursor.close()

  if servicos_empresa:
      print(f"\nLista de Serviços Vinculados à Empresa '{empresa[1]}':")
      for se in servicos_empresa:
          print(f"{se[0]}. Serviço: {se[2]}, Valor: {se[3]}")
      return servicos_empresa
  else:
      print("\nNenhum serviço vinculado à empresa.")
      return None
  
def pegar_servico_empresa_pelo_id(conn, id_servico_empresa):
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Servicos_empresa WHERE ID = %s', (id_servico_empresa,))
  servico_empresa = cursor.fetchone()
  cursor.close()

  if servico_empresa:
    return servico_empresa
  else:
     return None

def criar_servico_empresa(conn, id_empresa, id_servico, valor):
  cursor = conn.cursor()
  cursor.execute(
      '''
      INSERT INTO Servicos_empresa (ID_Empresa, ID_Servico, Valor)
      VALUES (%s, %s, %s)
      ''', (id_empresa, id_servico, valor))
  conn.commit()
  cursor.close()

  print("\nServiço vinculado à empresa criado com sucesso.")

def ler_servico_empresa(conn, id_servico_empresa):
  servico_empresa = pegar_servico_empresa_pelo_id(conn, id_servico_empresa)
  
  if servico_empresa:
      print("\nDetalhes do Serviço Vinculado à Empresa:")
      print(servico_empresa)
  else:
      print("\nServiço vinculado à empresa não encontrado.")

def atualizar_servico_empresa(conn, id_servico_empresa):
  valor = input("\nNovo Valor do Serviço Vinculado à Empresa: ")
  
  cursor = conn.cursor()
  cursor.execute('''
      UPDATE Servicos_empresa
      SET Valor=%s
      WHERE ID=%s
  ''', (valor, id_servico_empresa))

  conn.commit()
  cursor.close()
  
  print("\nServiço vinculado à empresa atualizado com sucesso.")

def deletar_servico_empresa(conn, id_servico_empresa):
  servico_empresa = pegar_servico_empresa_pelo_id(conn, id_servico_empresa)
  
  if servico_empresa:
    confirmacao = input(f"Tem certeza que deseja deletar o serviço vinculado à empresa ID {id_servico_empresa}? (S/N): ")

    if confirmacao.lower() == 's':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Servicos_empresa WHERE ID=%s", (id_servico_empresa,))
        conn.commit()
        cursor.close()

        print("\nServiço vinculado à empresa deletado com sucesso.")
    else:
        print("\nOperação de exclusão cancelada.")
  else:
      print("\nServiço vinculado à empresa não encontrado.")

def deletar_servicos_empresa(conn, id_empresa):
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Servicos_empresa WHERE ID_Empresa = %s', (id_empresa,))
  servicos_empresa = cursor.fetchall()

  if servicos_empresa:
    cursor.execute("DELETE FROM Servicos_empresa WHERE ID_Empresa=%s", (id_empresa,))
    conn.commit()
    
    print("\nServiços vinculados à empresa deletados com sucesso.")
  else:
    print("\nNenhum serviço vinculado à empresa para deletar.")

  cursor.close()

def menu_servicos_empresa(conn, empresa, id_empresa):
  while True:
    print(f"\n------ Gerenciar Serviços da Empresa '{empresa[1]}' ------")
    print("1. Listar Serviços Vinculados à Empresa")
    print("2. Vincular Novo Serviço à Empresa")
    print("3. Retirar Serviço da Empresa")
    print("0. Voltar ao Menu de Gerenciar Empresa")
    escolha_servicos = input("Escolha a opção: ")

    if escolha_servicos == '1':
      listar_servicos_empresa(conn, empresa, id_empresa)

    elif escolha_servicos == '2':
      servicos = listar_servicos(conn)

      if servicos:
        id_servico = input(
            "\nDigite o ID do Serviço que deseja vincular à empresa: ")
        valor = input("Digite o valor do serviço para a empresa: ")
        criar_servico_empresa(conn, id_empresa, id_servico, valor)
      else:
         print("Cadastre um serviço primeiro para então vinculá-lo à empresa.")

    elif escolha_servicos == '3':
      servicos = listar_servicos_empresa(conn, empresa, id_empresa)

      if servicos:
        id_servico_empresa = input("\nDigite o ID do Serviço da Empresa que deseja remover: ")
        deletar_servico_empresa(conn, id_servico_empresa)

    elif escolha_servicos == '0':
      break

    else:
      print("\nOpção inválida. Tente novamente.")
