import psycopg2

def get_conexao():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres.payjekqzziftigaiedar',
        password='MJrx1706#06',
        host='aws-1-us-east-2.pooler.supabase.com',
        port='6543'
    )
    return conn