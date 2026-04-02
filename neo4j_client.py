
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables from .env including pass and user name
load_dotenv() 

print(os.getenv("NEO4J_URI"))
print(os.getenv("NEO4J_USER"))
print(os.getenv("NEO4J_PASSWORD"))


class Neo4jClient:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USER"),
                os.getenv("NEO4J_PASSWORD")
            )
        )

    def run(self, query, params=None):
        with self.driver.session() as session:
            result = session.run(query, params)
            return [r.data() for r in result]

    def close(self):
        self.driver.close()