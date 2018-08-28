import sqlite3
conn = sqlite3.connect('QCDB.sqlite')
c = conn.cursor()

#Per base sequence quality, #Base	Mean	Median	Lower Quartile	Upper Quartile	10th Percentile	90th Percentile
#c.execute("""CREATE TABLE 'Per base sequence quality' (
#            '#Base' integer PRIMARY KEY,
#            Mean real,
#            Median real,
#            'Lower Quartile' real,
#            'Upper Quartile' real,
#            '10th Percentile' real,
#            '90th Percentile' real);""")
#conn.commit()
#conn.close()
#print c.fetchall()

#Per tile sequence quality #Tile	Base	Mean
#c.execute("""CREATE TABLE 'Per tile sequence quality' (
#            Tile integer PRIMARY KEY,
#            Base integer,
#            Mean real);""")
#print c.fetchall()

#Per sequence quality scores #Quality	Count
#c.execute("""CREATE TABLE 'Per sequence quality scores'(
#            Quality integer Primary Key,
#            Count real);""")
#print c.fetchall()

#Per base sequence content	#Base	G	A	T	C
#c.execute("""CREATE TABLE 'Per base sequence content'(
#            Base integer PRIMARY KEY,
#            G real,
#            A real,
#            T real,
#            C real);""")
#print c.fetchall()

#Per sequence GC content #GC Content
#c.execute("""CREATE TABLE 'Per sequence GC content'(
#            'GC Content' integer Primary Key,
#            Count real);""")
#print c.fetchall()

#Per base N content	pass Base	N-Count
#c.execute("""CREATE TABLE 'Per base N content'(
#            Base integer PRIMARY KEY,
#            COUNT real);""")
#print c.fetchall()

#Sequence Length Distribution #Length	Count
#c.execute("""CREATE TABLE 'Sequence Length Distribution'(
#            Length integer PRIMARY KEY,
#            Count real);""")
#print c.fetchall()

#Sequence Duplication Levels #Duplication Level	Percentage of deduplicated	Percentage of total

#            'Duplication Level' integer PRIMARY KEY,
#            'Percentage of deduplicated' real,
#            'Percentage of total' real);""")
#print c.fetchall()

#Adapter Content
##Position	Illumina Universal Adapter	Illumina Small RNA 3' Adapter
# Illumina Small RNA 5' Adapter 	Nextera Transposase Sequence	SOLID Small RNA Adapter
#c.execute("""CREATE TABLE 'Adapter Content'(
#            Position integer PRIMARY KEY,
#            'Illumina Small RNA 3 Adapter' real,
#            'Illumina Small RNA 5 Adapter' real,
#            'Nextera Transposase Sequence' real,
#            'SOLID Small RNA Adapter' real);""")
#print c.fetchall()

#Kmer Content
#Sequence	Count	PValue	Obs/Exp Max	Max Obs/Exp Position
#c.execute("""CREATE TABLE 'Kmer Content'(
#            Sequence text PRIMARY KEY,
#            COUNT integer,
#            PValue real,
#            'Max Obs/Exp Position' integer);""")
#print c.fetchall()
