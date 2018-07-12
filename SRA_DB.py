
import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()

taxon_id = raw_input("Enter taxon_id: ")


library_source = str(raw_input("Enter library_source: "))


instrument_model = raw_input("Enter instrument_model: ")


number_results = raw_input("Enter number number_results: ")


c.execute('SELECT run_accession FROM sra WHERE taxon_id == "{0}" AND library_source == "{1}" AND instrument_model == "{2}" LIMIT "{3}";'
.format(taxon_id, library_source, instrument_model, number_results))
print c.fetchall()
