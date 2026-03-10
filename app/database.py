from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Inicializacao( criacao de SCHEMA no banco de dados)
#SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DBNAME)')}"

SERVER_URL = "mysql+pymysql://root:admin@localhost"

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit



# Conexao com o banco de dados
#DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DBNAME)')}"

DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_api"

# Criar um "motor" que fara o gerenciamento da conexão
engine = create_engine(DATABASE_URL)

# Criando uma sessao para executar os comandos SQL
SenssionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria um objeto da base de dados manipulavel pelo python 
Base = declarative_base()

# injecao de dependencias: injeta a sessao do banco de dados
# em cada rota que for criada
def get_db():
    db = SenssionLocal()
    try:
        yield db
    finally:
        db.close()