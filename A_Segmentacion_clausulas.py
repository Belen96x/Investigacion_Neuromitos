import spacy

nlp = spacy.load("en_core_web_sm")

def segment_sentence(text):
    doc = nlp(text)
    clauses = []
    start_index = 0
    
    for token in doc:
        # Check if the token is a conjunction that separates clauses
        if token.dep_ == "cc" or token.dep_ == "mark":
            # Add the current clause to the list
            clause = doc[start_index:token.i+1]
            clauses.append(clause)
            start_index = token.i+1
    
    # Add the last clause to the list
    clause = doc[start_index:]
    clauses.append(clause)
    
    return clauses

#Chequear funcionamiento

texto = "He corrido por el parque que se encuentra al fondo de mi barrio"
clausulas = segment_sentence(texto)
print(clausulas)
