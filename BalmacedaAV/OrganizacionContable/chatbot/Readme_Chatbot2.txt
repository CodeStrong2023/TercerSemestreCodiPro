
***Chatbot con Inteligencia Artificial**
**Descripción**
Este proyecto es un chatbot básico que utiliza inteligencia artificial para responder a preguntas y mensajes del usuario. El chatbot utiliza el modelo de lenguaje de spaCy para procesar el lenguaje natural y un modelo de red neuronal para clasificar las intenciones del usuario.
**Requisitos**
Python 3.x
spaCy (versión 3.x)
TensorFlow (versión 2.x)
numpy (versión 1.x)
**Instalación**
Instale las dependencias necesarias con pip: pip install spacy tensorflow numpy
Descargue el modelo de lenguaje de spaCy para inglés: python -m spacy download en_core_web_sm
Ejecute el archivo chatbot.py para iniciar el chatbot
**Uso**
Inicie el chatbot ejecutando el archivo chatbot.py
Introduzca un mensaje o pregunta en la consola
El chatbot responderá con una respuesta adecuada
**Estructura del proyecto**
chatbot.py: archivo principal del chatbot que contiene la lógica de procesamiento de lenguaje natural y la red neuronal
intents.json: archivo que contiene las intenciones y respuestas del chatbot
**Funcionamiento**
El chatbot carga el modelo de lenguaje de spaCy y las intenciones del archivo intents.json
El usuario introduce un mensaje o pregunta en la consola
El chatbot procesa el mensaje utilizando el modelo de lenguaje de spaCy y lo clasifica en una de las intenciones definidas
El chatbot selecciona una respuesta aleatoria de las definidas para la intención clasificada
El chatbot devuelve la respuesta al usuario
**Limitaciones**
El chatbot solo entiende inglés
El chatbot solo puede responder a preguntas y mensajes que estén definidos en el archivo intents.json
El chatbot no tiene capacidad de aprendizaje automático, por lo que no puede mejorar su precisión con el tiempo
**Mejoras futuras**
Agregar soporte para múltiples idiomas
Implementar un algoritmo de aprendizaje automático para mejorar la precisión del chatbot
Agregar más intenciones y respuestas al archivo intents.json

