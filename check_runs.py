import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()

        ##experiment_ID on muliple/single runs##

#c.execute('SELECT COUNT (*) as "Number of Rows" FROM sra GROUP BY experiment_ID HAVING COUNT(experiment_ID) ==1;')<---
#got all (1,0) for return values

#TOTALROWS#####c.execute('SELECT COUNT(*) as "Number of Rows" FROM sra;')======[(4103273,)]

###c.execute('SELECT experiment_ID, COUNT(*) FROM sra GROUP BY experiment_ID HAVING COUNT (*) == 1;')===returns exp id w/counts
##experiment_ID # showing they appeared once --over 4 million exps
##c.execute ('SELECT COUNT(experiment_ID) FROM sra GROUP BY experiment_ID HAVING COUNT(experiment_ID) > 1;')==returns how many time it appears but no total
#c.execute('SELECT COUNT(experiment_ID) as "Number of Rows" FROM sra GROUP BY experiment_ID HAVING COUNT(*) >= 2;')==returns count
##c.execute('SELECT COUNT(experiment_ID) FROM sra WHERE (COUNT(experiment_ID) > 1);')

#TOTALEXP_IDc.execute('SELECT COUNT(experiment_ID) FROM sra;')==[(4102108,)]=====TOTAL experiment_ID
#c.execute('SELECT COUNT(DISTINCT study_ID) FROM sra;')==[(3635846,)]===TOTAL DISTINCT experiment_ID
c.execute('SELECT study_ID, COUNT(*) AS RecordCount FROM sra GROUP BY study_ID HAVING COUNT(*)>1;')


print len(c.fetchall())







# experiment_ID single run
#c.execute('SELECT COUNT(run_id), COUNT(experiment_ID) FROM sra GROUP BY run_id HAVING COUNT((experiment_ID)==1);')
#print c.fetchall()


# study_ID muliple runs
#c.execute('SELECT COUNT(run_id), COUNT(study_ID) FROM sra GROUP BY run_id HAVING COUNT((study_ID)>1);')
#print c.fetchall()
# study_ID single runs
#c.execute('SELECT COUNT(run_id), COUNT(study_ID) FROM sra GROUP BY run_id HAVING COUNT((study_ID)==1);')
#print c.fetchall()


#submission_ID
#c.execute('SELECT COUNT(run_id), submission_ID FROM sra GROUP BY run_id HAVING COUNT((submission_ID)>1) LIMIT 5;')
#print c.fetchall()
