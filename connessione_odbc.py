import pyodbc

# Dettagli della connessione
driver = '{MySQL ODBC 9.3 Unicode Driver}'  # Assicurati che corrisponda esattamente al nome del tuo driver
server = 'localhost'  # Solitamente 'localhost' per XAMPP
database = 'vino'  # Inserisci il nome del tuo database
username = 'root'  # Username predefinito di XAMPP MySQL
password = ''  # Password predefinita di XAMPP MySQL è spesso vuota
port = '3306'  # Porta predefinita di MySQL

# Costruisci la stringa di connessione
conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'PORT={port};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

conn = None
try:
    # Tenta di stabilire la connessione
    conn = pyodbc.connect(conn_str)
    print("Connessione ODBC stabilita con successo!")

    # Puoi eseguire qui le tue operazioni sul database
    # Ad esempio, creare un cursore e eseguire una query:
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    row = cursor.fetchone()
    if row:
        print(f"Versione del database: {row[0]}")

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"Errore durante la connessione ODBC: {sqlstate}")
    print(f"Dettagli dell'errore: {ex}")

finally:
    # Chiudi la connessione se è aperta
    if conn:
        conn.close()
        print("Connessione ODBC chiusa.")