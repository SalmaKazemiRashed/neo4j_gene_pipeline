from neo4j import GraphDatabase

class Neo4jClient:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            "bolt://localhost:7687",
            auth=("neo4j", "password")
        )

    def run(self, query, params=None):
        with self.driver.session() as session:
            result = session.run(query, params)
            return [r.data() for r in result]

    def close(self):
        self.driver.close()