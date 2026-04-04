import pandas as pd
from neo4j_client import Neo4jClient

db = Neo4jClient()  
df = pd.read_csv("data/cleaned_feature.csv")

def ingest():

    for _, row in df.iterrows():

        query = """
        MERGE (g:Gene {entrezgene_id: $id})
        SET g.symbol = $symbol,
            g.accession = $acc,
            g.aliases = $alias,
            g.description = $desc

        WITH g

        MERGE (expA:Experiment {name: "A"})
        MERGE (expB:Experiment {name: "B"})
        MERGE (expC:Experiment {name: "C"})
        MERGE (expD:Experiment {name: "D"})

        MERGE (mA:Measurement {gene_id: $id, exp: "A"})
        SET mA.count_decrease = $A_cd,
            mA.area_increase = $A_ai
        MERGE (g)-[:MEASURED_IN]->(mA)
        MERGE (mA)-[:FROM]->(expA)

        MERGE (mB:Measurement {gene_id: $id, exp: "B"})
        SET mB.count_decrease = $B_cd,
            mB.area_increase = $B_ai
        MERGE (g)-[:MEASURED_IN]->(mB)
        MERGE (mB)-[:FROM]->(expB)

        MERGE (mC:Measurement {gene_id: $id, exp: "C"})
        SET mC.count_decrease = $C_cd,
            mC.area_increase = $C_ai
        MERGE (g)-[:MEASURED_IN]->(mC)
        MERGE (mC)-[:FROM]->(expC)

        MERGE (mD:Measurement {gene_id: $id, exp: "D"})
        SET mD.count_decrease = $D_cd,
            mD.area_increase = $D_ai
        MERGE (g)-[:MEASURED_IN]->(mD)
        MERGE (mD)-[:FROM]->(expD)
        """

        db.run(query, {
        "id": row["entrezgene_id"],
        "symbol": row["entrezgene_symbols"],
        "acc": row["genbank_accession"],
        "alias": row["aliases"],
        "desc": row["description"],

        "A_cd": float(row["count_decrease_a"]),
        "A_ai": float(row["area_increase_a"]),
        "B_cd": float(row["count_decrease_b"]),
        "B_ai": float(row["area_increase_b"]),
        "C_cd": float(row["count_decrease_c"]),
        "C_ai": float(row["area_increase_c"]),
        "D_cd": float(row["count_decrease_d"]),
        "D_ai": float(row["area_increase_d"])
    })

if __name__ == "__main__":
    ingest()