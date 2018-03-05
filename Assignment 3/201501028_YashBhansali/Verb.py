import spacy
import json
nlp = spacy.load('en_core_web_sm')
json_data = open('data.json')
data = json.load(json_data)
Lyrics = ""
for i in range (0,100):
	doc = nlp(data[i]['Lyrics'])
	for np in doc:
		if np.pos_ == "VERB":  
			print (np.lemma_)
