
import sqlite3 as sql

USUARIO = 'j123'
NOME = 'Jonas'
SENHA = 'abd123456'
EMAIL = 'jonas@email.com'


DADOS = {
    '1': {'usuario': 'jonas1234', 'senha': 'abd12345', 'nome': 'jonas djones jonedes', 'email': 'jonas@email.com'},
    '2': {'usuario': 'jhon1', 'senha': 'abd12345', 'nome': 'jhon Raquel Gracies', 'email': 'jhon@email.com'},
    '3': {'usuario': 'Allan123', 'senha': 'abd12345', 'nome': 'Allan Touredes', 'email': 'allan@email.com'}
}

def create_db():
    conn = sql.connect('bd.db')
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    nome text
                )
                
                """)

    conn.commit()
    cur.close()
    conn.close()

def insert_usuario(usuario, senha, email):
    conn = sql.connect('bd.db')
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO Usuario (usuario, senha, email)
        VALUES (?, ?, ?)
        """,
        (usuario, senha, email)
        
    )
    
    conn.commit()
    cur.close()
    conn.close()


def validar_conta(usuario:str, senha:str) -> bool:
    if usuario == USUARIO and senha == SENHA:
        return True
    else:
        return False

def get_usuario():
    return USUARIO, SENHA, NOME, EMAIL



if __name__ == '__main__':
    insert_usuario(usuario='admin',
                   senha='admin',
                   email='admin@email.com')
    # create_db()