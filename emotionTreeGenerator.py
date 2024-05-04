import json
from anytree import Node, RenderTree

def build_tree(data, parent=None):
    node = Node(data['name'], parent=parent)
    if 'children' in data:
        for child_data in data['children']:
            build_tree(child_data, parent=node)
    return node

# Read JSON file
with open('emotionWheelTree.json') as f:
    json_data = json.load(f)

# Build the tree
root_node = build_tree(json_data)

# Print the tree structure
for pre, _, node in RenderTree(root_node):
    print("%s%s" % (pre, node.name))
