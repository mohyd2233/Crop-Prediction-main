import pickle as pkl
import sqlite3 as sql


conn = sql.connect('cropdata.db')
cur = conn.cursor()
cur.execute(f''' DELETE FROM CROP WHERE PREDICTED_CROP = "mango" ''')
conn.commit()