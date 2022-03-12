import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
row = c.execute("DELETE  SET balance = 100 WHERE id = 1")
conn.commit()
conn.close()
