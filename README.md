# neo4j_gene_pipeline

This project is in continuation of [cell_microscopy](https://github.com/SalmaKazemiRashed/Cell_Microscopy_project) project.
The results of genome-wide screen analysis gave us the normalized count and average area of nuclei fold change for all genes (18000 nodes.)
Here, I want to have an structured neo4j  graph database built upon the results of that experiment.

### Steps
The steps are :

* Load CSV (results are saved in .csv file)
* Build graph  (convert csv to neo4j graph database using cypher)
* Compute aggregates (The repeated experiments should be handled)
* Expose API (FastAPI) (make the pipeline a real production-like service)
* Query results 

### Nodes
here, we defined graph nodes as 
* genes 
* Experiment (A-B , C-D) (oxidative and non-oxidative stress)
* Measurments (per gene per experiment)

### Relationships
The relationships(edges) in the graph would be like:
```plaintext
(Gene)-[:MEASURED_IN]->(Measurement)-[:FROM_EXPERIMENT]->(Experiment)
```
This design is better than flat features linked to each node as it is scalable and we can see separation of biology vs measurment.

### CSV file
The csv file has following format.
```plaintext
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>entrezgene_id</th>
      <th>entrezgene_symbols</th>
      <th>genbank_accession</th>
      <th>aliases</th>
      <th>description</th>
      <th>count_decrease_a</th>
      <th>area_increase_a</th>
      <th>count_decrease_b</th>
      <th>area_increase_b</th>
      <th>count_decrease_c</th>
      <th>area_increase_c</th>
      <th>count_decrease_d</th>
      <th>area_increase_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7272</td>
      <td>TTK</td>
      <td>NM_003318</td>
      <td>TTK;CT96;ESK;FLJ38280;MPS1;MPS1L1;PYT</td>
      <td>TTK protein kinase</td>
      <td>0.512461</td>
      <td>1.093648</td>
      <td>0.713287</td>
      <td>1.157135</td>
      <td>0.700742</td>
      <td>1.048722</td>
      <td>0.708258</td>
      <td>1.125556</td>
    </tr>
  </tbody>
</table>
</div>
```