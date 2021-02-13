# Event Extractor using NLP

### Goal:
- Automatically gathering all relevant information regarding a user inputed event from a large corpus of data

### Event Definition:
- Detecting and extracting the subject of a terrorist or militant operation from textual data

### Data Source:
https://www.state.gov/reports/country-reports-on-terrorism-2019/
- 40 articles downloaded
- Saved in .txt format

### Two helper functions
- detect_event(doc, verb_list, dobj_list)
- Locates the root verb and checks if it is in verb_list
- Determines if root verb has direct object as its child and checks if it is in
dobj_list
- returns the root verb as event
- actor_extractor(event)
- Finds the nominal subject for root verb
- returns the actor of event
 
### Example
In Bangladesh, ISIS-affiliated terrorists claimed six IED attacks, five of which were directed against Bangladesh police.
<br><b>Actor</b>: ISIS-affiliated terrorists 
<br><b>Event</b>: claimed
<br><b>Direct object</b>: attacks

![displacy](https://github.com/Guluna/Event-Extractor-NLP-/blob/main/Displacy.png?raw=true)
 
