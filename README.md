## **QC-Database**
**Title:** QC Database Prototype\
**Contributors:** August Guang, Ashok Ragavendran, and Gail Golomb Mello\
**Description:**  The QCDatabase would form part of the QCKit suite. One component of the QCKit suite is quality control tools to run on Next Generation Sequencing (and perhaps Third Generation Sequencing) data. Another component is visualization of the results of the quality control tools. The final component is the QC Database, containing quality control results from public repositories such as NCBI, such that the results of the quality control tools can be compared and visualized against other similar sequencing runs. This allows the researcher to get a quantitative sense of the quality of their sequences, rather than relying on the researcher’s experiential knowledge about what constitutes high quality sequences or not for their particular organism or protocol. Users running the QCKit suite will also have the option to upload their quality control results into the database as another data point. The entire suite will be incorporated into bioflows, a bioinformatics workflow management tool, which will run quality control at all appropriate intervals, ideally each component of a workflow

## Dependencies

QCDB is written in Python, and beyond that has a few dependencies mostly relating to NCBI downloads. We rely on conda as a package manager to install the dependencies. The user can either set up a conda environment with the packages we use using `environment.yml`, or can manually run the commands below to install everything needed:

```
conda install sqlite3 sqlalchemy
conda install -c bioconda sra-tools fastqc
```

**License:** Licensed under GNU GPLv3 (LICENSE)
