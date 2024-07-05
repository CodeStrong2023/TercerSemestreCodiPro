
***Chatbot con Inteligencia Artificial***
**Descripción**
Este proyecto es un chatbot básico que utiliza inteligencia artificial para responder a preguntas y entradas del usuario. El chatbot utiliza un archivo JSON para cargar intenciones y respuestas predefinidas, y utiliza la biblioteca NLTK para tokenizar y lematizar las palabras. El modelo de aprendizaje automático se entrena con los patrones de entrada y salida, y se utiliza para predecir la intención del usuario y responder adecuadamente.
**Requisitos**
Python 3.x
NLTK (Natural Language Toolkit)
NumPy
Keras (para la creación del modelo de red neuronal)
**Estructura del proyecto**
intents.json: archivo que contiene las intenciones y respuestas predefinidas del chatbot
chatbot.py: archivo que contiene el código del chatbot
**Funcionamiento**
El chatbot carga las intenciones y respuestas predefinidas desde el archivo intents.json.
El usuario ingresa una entrada en la consola.
El chatbot tokeniza y lematiza la entrada utilizando NLTK.
El chatbot utiliza el modelo de aprendizaje automático para predecir la intención del usuario.
El chatbot selecciona una respuesta aleatoria desde la lista de respuestas correspondientes a la intención predicha.
El chatbot muestra la respuesta en la consola.
**Uso**
Ejecutar el archivo chatbot.py en la consola.
Ingresar una entrada en la consola (por ejemplo, "hola").
El chatbot responderá con una respuesta aleatoria correspondiente a la intención predicha.
**Notas**
El archivo intents.json debe estar en la misma carpeta que el archivo chatbot.py.
El modelo de aprendizaje automático se entrena con los patrones de entrada y salida, por lo que es importante tener un conjunto de datos suficientemente grande y diverso para entrenar el modelo.
El chatbot utiliza un umbral de error para determinar si una entrada es lo suficientemente similar a una intención predefinida. Si la entrada no se ajusta a ninguna intención, el chatbot no responderá.