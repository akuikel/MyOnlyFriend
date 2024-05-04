import json
from anytree import Node, RenderTree, PreOrderIter
from emotionTreeGenerator import EmotionNode

# Create the emotion tree from the JSON file
emotion_tree = EmotionNode('emotionWheelTree.json')

# Get the root node of the emotion tree
root_node = emotion_tree.get_root_node()

# Print the tree structure
emotion_tree.print_tree_structure()

# Define a function to find a node by name
def find_node_by_name(root, name):
    for node in PreOrderIter(root):
        if node.name == name:
            return node
    return None

# Find the node with the name "Hurt"
node = find_node_by_name(root_node, "Hurt")

if node:
    # Print the parent node if it exists
    if node.parent:
        print("Parent of '{node_name}': {parent_name}".format(node_name=node.name, parent_name=node.parent.name))
    else:
        print("No parent node found for '{node_name}'".format(node_name=node.name))

    # Print the child nodes if they exist
    if node.children:
        print("Children of '{node_name}': {children_names}".format(node_name=node.name, children_names=[child.name for child in node.children]))
    else:
        print("No child nodes found for '{node_name}'".format(node_name=node.name))
else:
    print("Node not found in the tree")
