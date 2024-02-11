import re
import networkx as nx
import pandas as pd

def add_missing_commas(json_string):
    # Define the JSON attributes in the order they are expected to appear
    attributes = ["source", "target", "semantics", "relation"]
    
    # For each attribute except the last one, add a comma if it's missing
    for i in range(len(attributes)-1):
        # This regex looks for the attribute, followed by any amount of whitespace, a colon,
        # then any characters until the next attribute is found, without a comma before it.
        pattern = rf'("{attributes[i]}":.*?)(?=\s*"{attributes[i+1]}")'
        # Replacement adds a comma at the end of the matched pattern
        replacement = r'\1,'
        json_string = re.sub(pattern, replacement, json_string, flags=re.DOTALL)
    
    return json_string


def get_dataframe_graph(triplets):
    edge_list = pd.DataFrame(triplets)
    G = nx.from_pandas_edgelist(edge_list, 'source', 'target', edge_attr=True, create_using=nx.MultiDiGraph())
    return edge_list, G