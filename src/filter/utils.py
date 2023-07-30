import spacy

#chargement du modèle
nlp = spacy.load()

def process_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

#Fonction pour remplir des listes 

