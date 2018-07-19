import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()

c.execute('SELECT COUNT(run_id), experiment_ID FROM sra GROUP BY run_id HAVING COUNT((experiment_ID)>1) LIMIT 5;')
print c.fetchall()

c.execute('SELECT COUNT(run_id), study_ID FROM sra GROUP BY run_id HAVING COUNT((study_ID)>1) LIMIT 5;')
print c.fetchall()

c.execute('SELECT COUNT(run_id), submission_ID FROM sra GROUP BY run_id HAVING COUNT((submission_ID)>1) LIMIT 5;')
print c.fetchall()
