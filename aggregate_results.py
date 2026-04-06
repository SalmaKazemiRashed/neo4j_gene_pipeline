from neo4j_client import Neo4jClient

db = Neo4jClient()

def compute_averages():

    query = """
    MATCH (g:Gene)-[:MEASURED_IN]->(m:Measurement)
    WITH g,
         avg(CASE WHEN m.exp IN ["A","B"] THEN m.area_increase END) AS avg_AB_area,
         avg(CASE WHEN m.exp IN ["C","D"] THEN m.area_increase END) AS avg_CD_area

    SET g.avg_AB_area = avg_AB_area,
        g.avg_CD_area = avg_CD_area
    """

    db.run(query)