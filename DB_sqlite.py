import sqlite3


# получение имён колонок
def table_columns(db, table_name):
    curs = db.cursor()
    sql = "select * from %s where 1=0;" % table_name
    curs.execute(sql)
    return [d[0] for d in curs.description]


def get_posts(name):
    with conn:
        cursor.execute(f"SELECT * FROM {name}")
        tbl = cursor.fetchall()
        for r in tbl:
            print(*r, sep="\t")

def get_posts2(name):
    with conn:
        cursor.execute(f"SELECT * FROM {name} ORDER BY WORD")
        tbl = cursor.fetchall()
        for r in tbl:
            print(*r, sep="\t")

if __name__ == '__main__' or __name__ == 'Test':
    conn = sqlite3.connect("Vocabulary.db")
    cursor = conn.cursor()

# Получение списка таблиц
#res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
#for name in res:
#    print(name[0])
#print(*table_columns(conn, "Settings"), sep="\t")
#get_posts("Settings")
    print(*table_columns(conn, "Stems"), sep="\t")
    get_posts2("Stems")
    conn.close()
