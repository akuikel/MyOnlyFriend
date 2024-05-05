import json
from anytree import Node, RenderTree, PreOrderIter
from emotionTreeGenerator import EmotionNode

# Create the emotion tree from the JSON file
emotion_tree = EmotionNode('emotionWheelTree.json')


print(emotion_tree.print_tree())



