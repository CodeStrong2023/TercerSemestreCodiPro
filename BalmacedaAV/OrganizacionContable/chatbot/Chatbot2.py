import spacy
import json
import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Cargar el modelo de lenguaje de spaCy
nlp = spacy.load('en_core_web_sm')

# Cargar intenciones del chatbot desde un archivo JSON
with open('intents.json') as file:
    intents = json.load(file)

words = []
classes = []
documents = []
ignore_words = ['?', '.', '!']

# Preprocesar las palabras y las intenciones
for intent in intents['intents']:
    for pattern in intent['patterns']:
        doc = nlp(pattern)
        w = [token.lemma_.lower() for token in doc]
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Eliminar palabras irrelevantes
words = [w for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

# Crear un modelo de aprendizaje automático
training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [word.lower() for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

# Aleatorizar el orden de los datos de entrenamiento
random.shuffle(training)
training = np.array(training)

# Crear el modelo de red neuronal
train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compilar el modelo
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Crear una función para responder a las entradas del usuario
def clean_up_sentence(sentence):
    doc = nlp(sentence)
    sentence_words = [token.lemma_.lower() for token in doc]
    return sentence_words

def bag_of_words(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % word)
    return np.array(bag)

def predict_class(sentence, model):
    p = bag_of_words(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res

# Probar el chatbot
while True:
    message = input("")
    response = chatbot_response(message)
    print(response)
