from cgitb import grey
import requests
import pandas as pd
import networkx as nx
import json
import nltk
from tqdm import tqdm
nltk.download('wordnet')
nltk.download('omw-1.4')

API_TOKEN = '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' # lol pls don't abuse my API key thanks
API_URL = 'https://api-inference.huggingface.co/models/dslim/bert-base-NER'
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

data = pd.read_json('webcrawling/notes.jl', lines=True)
G = nx.DiGraph()

lem = nltk.stem.WordNetLemmatizer()

for index, row in tqdm(data.iterrows()):
	output = query({'inputs': row['contents']})
	new_ent_names = []
	for out in output:
		word = out['word']
		score = out['score']
		group = out['entity_group']
		if word[0].isalpha() and len(word) > 1 and score > 0.99:
			word = lem.lemmatize(word, pos='n')
			new_ent_names.append(word)
	for name in new_ent_names:
		if name not in G.nodes:
			G.add_node(name, label=name)
		if G.get_edge_data(row['title'], name) is None:
			G.add_edge(row['title'], name, weight=1)
		else:
			G[row['title']][name]['weight'] += 1

with open('graphs/notes.json', 'w') as f:
	json.dump(nx.cytoscape_data(G), f)


	
