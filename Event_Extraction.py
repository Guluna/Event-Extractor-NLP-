import spacy
import os

nlp = spacy.load("en_core_web_sm")

pathToDocs = os.getcwd() + '/Data'

# Storing all articles in a list
list_docs = []
for f in os.listdir(pathToDocs):
    if f.endswith('.txt'):
        with open(pathToDocs + '/' + f, "r") as s:
            content = s.read()
            list_docs.append(content)

# Creating a spacy Generator object & converting it to list
processed_docs = list(nlp.pipe(list_docs))

# Hand made list of verbs and direct objects
verb_list = ["launch", "begin", "initiate", "start", "resume", "coordinate", "carry", "commit", "conduct", "claim"]
dobj_list = ["attack", "offensive", "operation", "assault", "activity"]

# detects if there is a root verb as well as direct object in the sentence
def detect_event(doc, verb_list, dobj_list):
    for word in doc:
        if word.dep_ == "ROOT" and word.lemma_ in verb_list:
            for subword in word.children:
                if subword.dep_ == "dobj" and subword.lemma_ in dobj_list:
                    return word, subword, word.sent
    else:
        return None, None, None

# extracts the subject of our "event" action verb
def actor_extractor(root):
    for child in root.children:
        if child.dep_ == "nsubj":
            nsubj = child.text
            nsubj_subtree = ''.join(w.text_with_ws for w in child.subtree if w.dep_ != 'prep' and w.dep_!='pobj').strip()   # removing prepositional and prepositional object dependencies from child subtree
    return nsubj_subtree


for doc in processed_docs:
    root, d_obj, sent = detect_event(doc, verb_list, dobj_list)
    if root != None:
        actor = actor_extractor(root)
        if actor:
            # print("Event Detected!")
            print("Actual sentence: ", sent, '\n')
            print("Actor: ", actor, '\n', "Event: ", root, '\n', "Direct object: ", d_obj)
            print('**********************************************************************************')



