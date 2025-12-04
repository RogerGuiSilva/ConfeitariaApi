import psycopg2

def get_conexao():
    return psycopg2.connect(
        host="db.zjiwvfcfqykiyclyejvj.supabase.co",
        port=5432,
        database="postgres",
        user="postgres",
        password="confeitaria"  
    )
