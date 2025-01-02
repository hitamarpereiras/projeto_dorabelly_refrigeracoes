import sqlite3
import os

def craete_folder():
    # sera criado o diretorio do banco de dados
    try:
        folder = 'Data'
        origin = os.path.join(folder, 'database')
        os.makedirs(origin, exist_ok=True)
        destiny = os.path.join(origin, 'database.db')

        return True, destiny
    
    except PermissionError:
        return False, 'Sem permissao do Sistema!'
    except Exception:
        return False, 'Erro ao criar pastas'
    
def connections():
    #bl recebe o booleano e data recebe o caminho 
    bl, data = craete_folder()
    if bl:
       try:
        conn = sqlite3.connect(data)
        return True, conn

       except Exception as e:
        return False, 'Erro ao criar o abnco de dados'
    else:
        return data
