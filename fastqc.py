import sqlalchemy
import subprocess

def download_fastq(run_accessions, outdir):
	"""
	Takes in run_accession numbers and downloads fastq files to dir from NCBI
	"""
	for accession in run_accessions:
		prefetch_cmd = 'prefetch {0} --force no'.format(accession)
		subprocess.call(prefetch_cmd, shell=True)
		fastq_cmd = 'fastq-dump {0} -O {1}'.format(accession, outdir)
		subprocess.call(fastq_cmd, shell=True)

def run_fastqc(fastq):
	"""
	Takes in fastq file and runs fastqc.
	"""
	fastqc_cmd = 'fastqc {0}'.format(fastq)

def db_insert(db, result):
	"""
	Takes in fastqc results file and inserts results into db
	"""

def db_access(run_accessions):
	"""
	Takes in run_accession numbers and returns fastqc results from database
	"""

