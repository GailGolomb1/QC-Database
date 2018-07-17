import argparse

parser = argparse.ArgumentParser(search_terms)

parser.add_argument('taxon_id', help= 'taxon id number will be an integer number refering to a species')
parser.add_argument('library_source', help= 'library source is either genomic or trasncriptomic')
parser.add_argument('instrument_model', help= 'model name of instrument used')
parser.add_argument('number_results', help= 'number of total results to be displayed for search')

search_terms = (taxon_id, library_source, instrument_model, number_results)
return parser.parse_args()
