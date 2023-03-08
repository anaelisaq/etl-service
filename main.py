import pandas as pd
from validate_docbr import CPF, CNPJ
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import contextlib

class Validator:
    def __init__(self):
        self.cpf = CPF()
        self.cnpj = CNPJ()

    def cpf_is_valid(self, cpf_number):
        return 'valid document' if self.cpf.validate(str(cpf_number)) else 'invalid, try again.'

    def cnpj_is_valid(self, cnpj_number):
        cnpj_stringfy = str(cnpj_number)
        if len(cnpj_stringfy) == 18:
            return 'valid document' if self.cnpj.validate(cnpj_stringfy) else 'invalid, try again.'
        else:
            return 'dont have a cnpj number'

validator = Validator()

columns = ['CPF', 'PRIVATE','INCOMPLETO','DATA_DA_ULTIMA_COMPRA','TICKET_MEDIO','TICKET_DA_ULTIMA_COMPRA', 'LOJA_MAIS_FREQUENTE', 'LOJA_DA_ULTIMA_COMPRA']
df = pd.read_csv("base_teste.txt", skiprows=1, header=None, delim_whitespace=True,names=columns)

df[['CPF_VALIDO', 'CNPJ_LOJA_MAIS_FREQUENTE_VALIDO', 'CNPJ_LOJA_DA_ULTIMA_COMPRA_VALIDO']] = df.applymap(
    lambda x: validator.cpf_is_valid(x) if 'CPF' in x.name else validator.cnpj_is_valid(x)
)

docker_db = 'postgresql://neoway:neoway@host.docker.internal:5432/dbneoway'

engine = create_engine(
    docker_db,
    pool_pre_ping=True
)

def get_conn():
    conn = engine.connect()
    try:
        yield conn
    finally:
        conn.close()

try:
    with get_conn() as conn:
        df.to_sql(
            name='dbneoway',
            schema='public',
            con=conn,
            if_exists='append',
            index=False,
            chunksize=10000,
            method='multi'
        )
        print('completed service')
except OperationalError as e:
    print(f"error connecting to database: {str(e)}")