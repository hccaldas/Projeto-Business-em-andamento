import mysql.connector
from mysql.connector import Error

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Rastafari1@',
            database='vendas_db'
        )
        if conexao.is_connected():
            print('Conexão ao MySQL realizada com sucesso!')
        return conexao
    except Error as e:
        print(f'Erro ao conectar ao MySQL: {e}')
        return None