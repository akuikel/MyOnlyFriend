import json
import os
from emotionTreeGenerator import EmotionNode
import google.generativeai as genai

# Configure the Google API key
os.environ['GOOGLE_API_KEY'] = "--IW7k"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the emotion tree and Gemini model
emotion_tree = EmotionNode('emotionWheelTree.json')
model = genai.GenerativeModel('gemini-pro')

# Template and data setup
prompt_template = '''
Analyze this journal entry and identify the emotions present, using the emotion wheel. Return the response in a single list.
Journal Entry:
{journal_entry}

Emotion List:
{emotion_list}

Return the response in a single list
'''

journal_entry = '''
i met Brock today at the DarkEngineOffice and he showed us something fascinating.
'''

emotion_list = [str(emotion) for emotion in emotion_tree.get_all_emotions()]

# Create the prompt for the Gemini API
prompt = prompt_template.format(journal_entry=journal_entry, emotion_list=", ".join(emotion_list))

# Generate content using the Gemini API
response = model.generate_content(prompt)
#print("Response text:", response.text)

identified_emotions = [line.strip('- ').strip() for line in response.text.split('\n') if line.strip()]
#print(identified_emotions)

emotionsPath= {}

for emotion in identified_emotions:
    detail= emotion_tree.get_node_details(emotion)
    if detail:
        emotionsPath[emotion] = detail

#print(emotionsPath)

output_prompt='''
Below I have included the emotion wheel hierarchy for each of the << IDENTIFIED EMOTIONS >> in my << JOURNAL ENTRY >>.

Using your expert knowledge as a psychologist and therapist to help me:

1. Use emotional intelligence to trace my emotions back to the root
2. Deepen my emotions and move through the children nodes, ideally finding release in the depening

Identify Emotions: Review the journal entry provided and identify the primary emotions expressed. These emotions should align with the emotion wheel hierarchy.
Deepen Understanding: Once you've identified the emotions, delve deeper into each one, considering its nuances and potential sub-emotions. This will help uncover a more comprehensive understanding of the writer's emotional state.
Provide Guidance: Based on the identified emotions, offer empathetic guidance and practical advice to assist the writer in navigating through their emotions effectively. Approach your response with the tone and style of a caring therapist.
Be specific in your advice, and show your thinking step-by-step. Use the tone and style of an empathetic, caring therapist.


Format your response as Markdown, omitting any pre or post text.
You don't have to write opening and ending salutations. Just the middle content only
Be specific in your advice, and show your thinking step-by-step. Use the tone and style of an empathetic, caring therapist.

Start by saying "From your journal entry, it's clear you're experiencing intense emotions related to your *what user said happened*. 
Your words convey a strong sense of *all the identified emotions*." Then begin to discuss *all the identified emotions* also explaining about it's origin (parent of the node)

NICELY FORMAT THE OUTPUT IN AN ATTRACTIVE WAY!!!!

<< JOURNAL ENTRY >>
{journal_entry}

<< IDENTIFIED EMOTIONS >>
{identified_emotions}
'''

prompt= output_prompt.replace("{journal_entry}",journal_entry)
prompt= prompt.replace("{identified_emotions}",json.dumps(emotionsPath))

response = model.generate_content(prompt)

print(response.text)


