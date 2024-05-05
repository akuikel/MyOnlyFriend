import json
from anytree import Node, PreOrderIter, RenderTree

class EmotionNode   :
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
        self.root = self.build_tree(data)

    def build_tree(self, data, parent=None):
        node = Node(data['name'], parent=parent)
        for child in data.get('children', []):
            self.build_tree(child, node)
        return node

    def find_node(self, name):
        for node in PreOrderIter(self.root):
            if node.name == name:
                return node
        return None

    def get_node_details(self, name):
        node = self.find_node(name)
        if node:
            path_to_root = [n.name for n in node.path]
            children = [child.name for child in node.children]
            return {
                'path': path_to_root,
                'children': children
            }
        else:
            return None

    def get_all_emotions(self):
        # Corrected from `self.root` to `self.root_node`
        return [node.name for node in PreOrderIter(self.root)]
    
    def print_tree(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))


