# neo4j_gene_pipeline

This project is in continuation of [cell_microscopy](https://github.com/SalmaKazemiRashed/Cell_Microscopy_project) project.
The results of genome-wide screen analysis gave us the normalized count and average area of nuclei fold change for all genes (18000 nodes.)
Here, I want to have an structured neo4j  graph database built upon the results of that experiment.

The steps are :

* Load CSV (results are saved in .csv file)
* Build graph  (convert csv to neo4j graph database using cypher)
* Compute aggregates (The repeated experiments should be handled)
* Expose API (FastAPI) (make the pipeline a real production-like service)
* Query results 