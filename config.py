import mysql.connector, os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

def conectar():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        auth_plugin="mysql_native_password"
    )
    return conexao
