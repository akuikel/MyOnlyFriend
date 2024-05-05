import openai
import json
from emotionTreeGenerator import EmotionNode

emotion_tree = EmotionNode('emotionWheelTree.json')
openai.api_key= ''

prompt_template= '''
Act as an expert psychologist who specializes in emotional intelligence.
Your job is to analyze my << JOURNAL ENTRY >> and identify which << EMOTIONS >> are present. These emotions come from my emotion wheel. Any emotions you identify MUST come the << EMOTIONS >> list. If you identify an emotion that is NOT present in the emotion list, use the most similar emotion from the list.

Omit any pre and post-text in your response. Format your response as a JSON list using the << JSON TEMPLATE >>.
Omit any pre and post-text in your response.
<< JOURNAL ENTRY >>
{journal_entry}

<< EMOTIONS >>
{emotion_list}

<< JSON TEMPLATE >>
{
	"emotions": []
}
'''

journal_entry= '''
i feel like the end of the world because my girlfriend broke up with me as she saw a text between me and my ex. i love my girlfriend a lot. this was a mistake from my side. hope she forgives but it's been already over a month.
'''

emotionList= [str(emotions) for emotions in emotion_tree.get_all_emotions()]

prompt= prompt_template.replace("{journal_entry}",journal_entry)
prompt= prompt.replace("{emotion_list}",",".join(emotionList))

completion = openai.chat.completions.create(
    model="gpt-4",
    temperature=0.7,
    messages=[{
        "role": "user",
        "content": prompt
    }]
)

output = json.loads(completion.choices[0].message.content)
identified_emotions = output["emotions"]

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



<< JOURNAL ENTRY >>
{journal_entry}

<< IDENTIFIED EMOTIONS >>
{identified_emotions}
'''

prompt= output_prompt.replace("{journal_entry}",journal_entry)
prompt= prompt.replace("{identified_emotions}",json.dumps(emotionsPath))

completion = openai.chat.completions.create(
    model="gpt-4",
    temperature=0.7,
    messages=[{
        "role": "user",
        "content": prompt
    }]
)
response = completion.choices[0].message.content
print(response)