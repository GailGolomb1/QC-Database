import argparse
parser = argparse.ArgumentParser()
import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()


def search_terms():
    taxon_id = raw_input("Enter taxon_id: ")

    library_source = str(raw_input("Enter library_source: "))

    instrument_model = raw_input("Enter instrument_model: ")

    number_results = raw_input("Enter number number_results: ")

def  search_db():
    ('SELECT run_accession FROM sra WHERE taxon_id == "{0}" AND library_source == "{1}" AND instrument_model == "{2}" LIMIT "{3}";'
    .format(taxon_id, library_source, instrument_model, number_results))

def main (search_terms, search_db):
    parser.add_argument('taxon_id', help= 'taxon id number will be an integer number referring to a species')
    parser.add_argument('library_source', help= 'library source is either genomic or transcriptomic')
    parser.add_argument('instrument_model', help= 'model name of instrument used')
    parser.add_argument('number_results', help= 'number of total results to be displayed for search')

    args = parser.parse_args()
    search_terms = ([args.taxon_id, args.library_source, args.instrument_model, args.number_results])

    return search_terms

main(search_terms, search_db)
