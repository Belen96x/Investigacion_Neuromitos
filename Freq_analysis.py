#Import of libraries

import string
import spacy
import es_core_news_sm

#Remove ortographic symbols of text.

test_str = """Garantizar los derechos de niños y adolescentes como una prioridad a pesar de la pandemia es una de las opciones que muchos países tomaron. Saben que de ellos depende el futuro, que su salud física y emocional se resiente con las escuelas cerradas, que hay pérdidas de aprendizaje que no se recuperan y que es difícil sostener la economía con los niños en casa. (32) 
La continuidad de la educación presencial ha sido tanto una realidad como una prioridad explícita para los gobiernos y las sociedades de múltiples países en tiempos del COVID-19, desde los más desarrollados hasta otros subdesarrollados (110)
Sin embargo, las experiencias de apertura de escuelas en el mundo y la evidencia sobre los establecimientos educativos como espacios relativamente seguros no parecían llegar a las autoridades argentinas ni a gran parte de los gremios docentes (84) [ellos]
La reapertura gradual de las clases presenciales a partir de septiembre y octubre en Colombia, Brasil y Chile fue más extendida que en Argentina, y sus planes son más claros para 2021, al igual que en países como Paraguay o México. En estas naciones, el discurso de la vacuna como condición nunca existió, y los ministros de Educación no se alinean con las posturas de los gremios docentes (133) [ellos]
"""

clean_str = test_str.translate (str.maketrans('','', string.punctuation))

print(clean_str)

#Rewrite each word in lower caps

lower_case_str = clean_str.lower()

print(lower_case_str)

#Lematize each word of the string. Turn into a list already

nlp = spacy.load('es_core_news_sm')

doc = nlp(lower_case_str)

lemmas = [tok.lemma_.lower() for tok in doc]

print(lemmas)

#Calculate word frequency

word_frecuency = []

for w in lemmas:
  word_frecuency.append(lemmas.count(w))

frecuency = str(list(zip(lemmas, word_frecuency)))

print(frecuency)

#Esto es una modificacion :)
