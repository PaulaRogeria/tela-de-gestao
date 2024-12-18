import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados MySQL
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin",
            database="banco",
            port=3306,
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida ao MySQL!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Função para criar (inserir) um novo aluno
def criar_Nome(NOME_DO_ALUNO, QUANTIDADE_DE_ACERTOS_LINGUAGENS,
               QUANTIDADE_DE_ACERTOS_NATUREZA, QUANTIDADE_DE_ACERTOS_HUMANAS,
               QUANTIDADE_DE_ACERTOS_MATEMATICA, TURMA, NOTA_FINAL):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            # Comando SQL para inserir dados
            query = """INSERT INTO tb_alunos (
                NOME_DO_ALUNO, 
                QUANTIDADE_DE_ACERTOS_LINGUAGENS, 
                QUANTIDADE_DE_ACERTOS_NATUREZA, 
                QUANTIDADE_DE_ACERTOS_HUMANAS, 
                QUANTIDADE_DE_ACERTOS_MATEMATICA, 
                TURMA, 
                NOTA_FINAL
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            
            # Executando o comando
            cursor.execute(query, (
                NOME_DO_ALUNO,
                QUANTIDADE_DE_ACERTOS_LINGUAGENS,
                QUANTIDADE_DE_ACERTOS_NATUREZA,
                QUANTIDADE_DE_ACERTOS_HUMANAS,
                QUANTIDADE_DE_ACERTOS_MATEMATICA,
                TURMA,
                NOTA_FINAL
            ))
            
            # Confirmar a inserção
            conexao.commit()
            print("Aluno inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            # Fechar cursor e conexão
            cursor.close()
            conexao.close()
            print("Conexão fechada.")

# Exemplo de uso da função
criar_Nome("Maria Souza", 9, 8, 7, 10, "Turma B", 8)

