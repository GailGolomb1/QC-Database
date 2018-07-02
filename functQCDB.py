import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()
c.execute ('SELECT Taxon_id, Library_source, Instrument_model FROM sra LIMIT 10;')
print c.fetchall()
