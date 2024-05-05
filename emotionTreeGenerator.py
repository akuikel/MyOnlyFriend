import json
from anytree import Node, RenderTree, PreOrderIter

# Define EmotionNode class
class EmotionNode:
    def __init__(self, json_file):
        with open(json_file) as f:
            self.data = json.load(f)
        self.node = self.build_tree(self.data)
        self.root_node = self.get_root_node()

    def build_tree(self, data, parent=None):
        node = Node(data['name'], parent=parent)
        if 'children' in data:
            for child_data in data['children']:
                self.build_tree(child_data, parent=node)
        return node

    def get_root_node(self):
        node = self.node
        while node.parent:
            node = node.parent
        return node
    
    def get_all_emotions(self):
        return [node.name for node in PreOrderIter(self.root_node) if node.is_root == False]

    def print_tree_structure(self):
        for pre, _, node in RenderTree(self.root_node):
            print("%s%s" % (pre, node.name))

# Usage example
if __name__ == "__main__":
    emotion_tree = EmotionNode('emotionWheelTree.json')
    emotion_tree.print_tree_structure()
