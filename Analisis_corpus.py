import spacy
from spacy.tokens import Doc
import variable_corpus
import csv
import textacy

string = variable_corpus.baratta_cap_4

nlp = spacy.load("es_core_news_sm")
doc = nlp(string)

assert doc.has_annotation("SENT_START")
results = []
for sent in doc.sents:
    results.append([sent.text])


with open("Oraciones_Cap_4_Baratta.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

