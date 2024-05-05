import openai
import json
from emotionTreeGenerator import EmotionNode

emotion_tree = EmotionNode('emotionWheelTree.json')

emotionList= emotion_tree.get_all_emotions()

#  print(emotionList)
