from neo4j_client import Neo4jClient

db = Neo4jClient()

# -----------------------------
# Averages
# -----------------------------
def get_averages():
    #query = """
    #MATCH (g:Gene)-[:MEASURED_IN]->(m:Measurement)
    #WITH g,
    #     avg(CASE WHEN m.exp IN ["A","B"] THEN m.area_increase END) AS avg_AB_area,
    #     avg(CASE WHEN m.exp IN ["A","B"] THEN m.count_decrease END) AS avg_AB_count,
    #     avg(CASE WHEN m.exp IN ["C","D"] THEN m.area_increase END) AS avg_CD_area,
    #     avg(CASE WHEN m.exp IN ["C","D"] THEN m.count_decrease END) AS avg_CD_count

    #RETURN g.symbol AS gene,
    #       avg_AB_area, avg_AB_count,
    #       avg_CD_area, avg_CD_count
    #Limit 100
    #"""

    query = """
    MATCH (g:Gene)
    RETURN g.symbol AS gene,
           g.avg_AB_area AS avg_AB_area,
           g.avg_AB_count AS avg_AB_count,
           g.avg_CD_area AS avg_CD_area,
           g.avg_CD_count AS avg_CD_count
    LIMIT 50
    """
    return db.run(query)



# -----------------------------
# Top genes (strong effect)
# -----------------------------
def top_genes():

    #query = """
    #MATCH (g:Gene)-[:MEASURED_IN]->(m:Measurement)
    #WITH g,
    #     avg(CASE WHEN m.exp IN ["A","B"] THEN m.area_increase END) AS avg_AB_area,
    #     avg(CASE WHEN m.exp IN ["A","B"] THEN m.count_decrease END) AS avg_AB_count,
    #     avg(CASE WHEN m.exp IN ["C","D"] THEN m.area_increase END) AS avg_CD_area,
    #     avg(CASE WHEN m.exp IN ["C","D"] THEN m.count_decrease END) AS avg_CD_count

    #WHERE 
    #    avg_AB_area > 1 AND avg_CD_area > 1 AND
    #    avg_AB_count < 0.5 AND avg_CD_count < 0.5
    #MATCH (g)-[r:MEASURED_IN]->(m)

    #RETURN g, r, m,
    #    avg_AB_area, avg_CD_area,
    #    avg_AB_count, avg_CD_count
    #LIMIT 100
    #"""

    #RETURN g.symbol AS gene,
    #       avg_AB_area, avg_CD_area,
    #       avg_AB_count, avg_CD_count
    #ORDER BY avg_AB_area DESC
    #LIMIT 50
    #"""
    ### After add the average values to each gene node as a feature the queries become simpler and no need to calculate average every time
    query = """
    MATCH (g:Gene)
    WHERE 
        (g.avg_AB_area > 1.5 AND g.avg_AB_count < 0.5) OR (g.avg_CD_area > 1.5 AND g.avg_CD_count < 0.5)

    RETURN g.symbol AS gene,
           g.avg_AB_area AS avg_AB_area,
           g.avg_CD_area AS avg_CD_area,
           g.avg_AB_count AS avg_AB_count,
           g.avg_CD_count AS avg_CD_count,
           g.A_cd AS A_cd,
           g.B_cd AS B_cd,
           g.C_cd AS C_cd,
           g.D_cd AS D_cd
    ORDER BY g.avg_AB_area DESC
    LIMIT 1000
    """
    return db.run(query)

    
    



# -----------------------------
# Flexible filtering
# -----------------------------
def filter_genes(area_min, area_max, count_min, count_max):
    #query = """
    #MATCH (g:Gene)-[:MEASURED_IN]->(m:Measurement)
    #WITH g,
    #     avg(CASE WHEN m.exp IN ["A","B"] THEN m.area_increase END) AS avg_AB_area,
    #     avg(CASE WHEN m.exp IN ["A","B"] THEN m.count_decrease END) AS avg_AB_count,
    #     avg(CASE WHEN m.exp IN ["C","D"] THEN m.area_increase END) AS avg_CD_area,
    #     avg(CASE WHEN m.exp IN ["C","D"] THEN m.count_decrease END) AS avg_CD_count

    #WHERE 
    #    avg_AB_area > $area_min AND avg_AB_area < $area_max AND
    #    avg_CD_area > $area_min AND avg_CD_area < $area_max AND
    #    avg_AB_count > $count_min AND avg_AB_count < $count_max AND
    #    avg_CD_count > $count_min AND avg_CD_count < $count_max

    #RETURN g.symbol AS gene,
    #       avg_AB_area, avg_CD_area,
    #       avg_AB_count, avg_CD_count
    #LIMIT 100
    #"""
    query = """
    MATCH (g:Gene)
    WHERE 
        g.avg_AB_area > $area_min AND g.avg_AB_area < $area_max AND
        g.avg_CD_area > $area_min AND g.avg_CD_area < $area_max AND
        g.avg_AB_count > $count_min AND g.avg_AB_count < $count_max AND
        g.avg_CD_count > $count_min AND g.avg_CD_count < $count_max

    RETURN g.symbol AS gene,
           g.avg_AB_area AS avg_AB_area,
           g.avg_CD_area AS avg_CD_area,
           g.avg_AB_count AS avg_AB_count,
           g.avg_CD_count AS avg_CD_count
    LIMIT 100
    """
    return db.run(query, {
        "area_min": area_min,
        "area_max": area_max,
        "count_min": count_min,
        "count_max": count_max
    })

