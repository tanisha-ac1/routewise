
import osmnx as ox
import networkx as nx

print("Downloading Chandigarh road network...")

G = ox.graph.graph_from_place(
    "Chandigarh, India",
    network_type="drive",
    simplify=True
)

print("Road network downloaded successfully!")
print("Number of intersections:", len(G.nodes))
print("Number of road connections:", len(G.edges))

ox.io.save_graphml(G, "chandigarh.graphml")

print("Road network saved as chandigarh.graphml")
