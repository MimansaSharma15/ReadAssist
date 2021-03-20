import sqlite3

def summarydb(path :str):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cmd = 'CREATE TABLE IF NOT EXISTS summary_tbl(Email TEXT, Summary TEXT)'
    cur.execute(cmd)
    conn.commit()

def insertsummary(tablename : str, email : str, summary : str, path :str):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    values = (email, summary)
    cmd =f'INSERT INTO {tablename} VALUES{values}' 
    print(cmd)

    cur.execute(cmd)
    conn.commit()

def getsummary(email : str, path : str):
    
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    sql = f"SELECT Summary FROM summary_tbl WHERE Email = '{email}' "
    cur.execute(sql)
    complete_summary = cur.fetchall()

    return complete_summary


    
if __name__ == '__main__':
    summarydb()
    insertsummary('summary_tbl', 'at8029srmist', 'SOMEONE', path='../app.db')
    