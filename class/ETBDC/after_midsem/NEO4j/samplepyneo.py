from py2neo import Graph, Node, Relationship

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4j123"))

# Create a node
node_a = Node("Person", name="Alice")
node_b = Node("Person", name="Bob")

# Create a relationship
relationship = Relationship(node_a, "KNOWS", node_b)

# Merge nodes and relationship into the graph
graph.merge(node_a, "Person", "name")
graph.merge(node_b, "Person", "name")
graph.merge(relationship)

# Query the graph
#query = "MATCH (p:Person)-[r:KNOWS]->(q:Person) RETURN p, r, q"
#result = graph.run(query)

# Print the result
#for record in result:
#    print(record)


















