
import sqlite3 as sql


PATH_DATABASE = 'dataBase.db'

class const:
    ID = 'id'
    USUARIO = 'usuario'
    SENHA = 'senha'
    EMAIL ='email'
    NOME = 'nome'
    MENSAGEM = 'mensagem'

    
def create_db():
    conn = sql.connect(PATH_DATABASE)
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    email TEXT NOT NULL,
                    nome text,
                    mensagem text
                )
                
                """)

    conn.commit()
    cur.close()
    conn.close()

def insert_usuario(usuario:str, senha:str, email:str) ->None:
    conn = sql.connect(PATH_DATABASE)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO Usuario (usuario, senha, email)
        VALUES (?, ?, ?)
        """,
        (usuario, senha, email,)
        
    )
    
    conn.commit()
    cur.close()
    conn.close()
    


def validar_conta(usuario:str, senha:str):
    '''return id '''
    # Conectando ao banco de dados
    conn = sql.connect(PATH_DATABASE)
    cursor = conn.cursor()

    # Consulta SQL para verificar se o usuário existe e a senha corresponde
    query = "SELECT id FROM Usuario WHERE usuario = ? AND senha = ?"
    
    # Executando a consulta
    cursor.execute(query, (usuario, senha))
    
    # Obtendo o resultado
    resultado = cursor.fetchone()
    
    # Fechando a conexão
    conn.close()
    
    # Retornando o ID do usuário ou None se não encontrado
    return resultado[0] if resultado else None




def get_usuarioByID(id) -> dict:
    
    conn = sql.connect(PATH_DATABASE)
    cur = conn.cursor()
    cur.row_factory = sql.Row #type:ignore

    query = ''' SELECT * 
                FROM Usuario 
                WHERE id = ?'''

    cur.execute(query, (id,))
    r = cur.fetchone()
    # r = cur.fetchall()

    conn.close()
    return dict(r)

# def update_user(id, senha=None, email=None, nome=None, mensagem=None):

def update_email(id, email):
    conn = sql.connect(PATH_DATABASE)
    cur = conn.cursor()

    query = '''UPDATE Usuario
                SET email = ?
                WHERE id = ?'''
    cur.execute(query,(email, id))
    conn.commit()
    conn.close()
    
def update_senha(id, senha):
    conn = sql.connect(PATH_DATABASE)
    cur = conn.cursor()

    query = '''UPDATE Usuario
                SET senha = ?
                WHERE id = ?'''
    cur.execute(query,(senha, id))
    conn.commit()
    conn.close()
    
def update_nome(id, nome):
    conn = sql.connect(PATH_DATABASE)
    cur = conn.cursor()
    nome = nome.title()
    query = '''UPDATE Usuario
                SET nome = ?
                WHERE id = ?'''
    cur.execute(query,(nome, id))
    conn.commit()
    conn.close()
    
def update_mensagem(id, mensagem):
    conn = sql.connect(PATH_DATABASE)
    cur = conn.cursor()

    query = '''UPDATE Usuario
                SET mensagem = ?
                WHERE id = ?'''
    cur.execute(query,(mensagem, id))
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    create_db()
    
    id = validar_conta('jonas', '123')
    print(id)
    
    print()
    print(get_usuarioByID(2))
    # update_email(2, 'jonas@email.com')
    update_nome(2, 'jonas coder')
    print(get_usuarioByID(2))
    # create_db()