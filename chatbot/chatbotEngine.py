import nltk
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder

from tensorflow.keras import Sequential, models
from tensorflow.keras.layers import Dense, Dropout

import random
import time

import os

# downloading model to tokenize message
nltk.download('punkt')
# downloading stopwords
nltk.download('stopwords')
# downloading wordnet, which contains all lemmas of english language
nltk.download('wordnet')

stop_words = stopwords.words('english')

# get the path in which intents file is stored
intents_path = os.path.dirname(__file__)


def clean_corpus(corpus):
    """
        Cleans the corpus downloaded above and returns the cleaned corpus
    """

    # lowering every word in text
    corpus = [doc.lower() for doc in corpus]
    cleaned_corpus = []

    stop_words = stopwords.words('english')
    wordnet_lemmatizer = WordNetLemmatizer()

    # iterating over every text
    for doc in corpus:
        # tokenizing text
        tokens = word_tokenize(doc)
        cleaned_sentence = []
        for token in tokens:
            # removing stopwords, and punctuation
            if token not in stop_words and token.isalpha():
                # applying lemmatization
                cleaned_sentence.append(wordnet_lemmatizer.lemmatize(token))
        cleaned_corpus.append(' '.join(cleaned_sentence))
    return cleaned_corpus


with open(intents_path + '/intents.json') as file:
    intents = json.load(file)

corpus = []
tags = []
for intent in intents['intents']:
    # taking all patterns in intents to train a neural network
    for pattern in intent['patterns']:
        corpus.append(pattern)
        tags.append(intent['tag'])

cleaned_corpus = clean_corpus(corpus)


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_corpus)


encoder = OneHotEncoder()
y = encoder.fit_transform(np.array(tags).reshape(-1, 1))

# ------------------------------ Creation and training of the nural network model --------------------------------------- #


model = Sequential([
    Dense(128, input_shape=(X.shape[1],), activation='relu'),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(y.shape[1], activation='softmax')
])

model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.summary()

# if os.path.exists('chatbotModel'):
#     models.load_model("chatbotModel")
# else:
history = model.fit(X.toarray(), y.toarray(), epochs=200, batch_size=1)
# model.save("chatbotModel")

# --------------------------------------------- Prediction of bot reponses ---------------------------------------------- #

# if prediction for every tag is low, then we want to classify that message as noanswer
INTENT_NOT_FOUND_THRESHOLD = 0.40


def predict_intent_tag(message):
    """
        actual prediction of the intents and returns the response tag which will later
        return a random input from the tag responses
    """

    message = clean_corpus([message])
    X_test = vectorizer.transform(message)
    y = model.predict(X_test.toarray())
    # if probability of all intent is low, classify it as noanswer
    if y.max() < INTENT_NOT_FOUND_THRESHOLD:
        return 'noanswer'

    prediction = np.zeros_like(y[0])
    prediction[y.argmax()] = 1
    tag = encoder.inverse_transform([prediction])[0][0]
    return tag


def get_intent(tag):
    """
      To return complete intent from intent tag
    """

    for intent in intents['intents']:
        if intent['tag'] == tag:
            return intent


def perform_action(action_code, intent):
    """
      Function to perform an action which is required by intent
    """

    if action_code == 'CHECK_ORDER_STATUS':
        print('\n Checking database \n')
        time.sleep(2)
        order_status = ['in kitchen', 'with delivery executive']
        delivery_time = []
        return {'intent-tag': intent['next-intent-tag'][0],
                'order_status': random.choice(order_status),
                'delivery_time': random.randint(10, 30)}

    elif action_code == 'ORDER_CANCEL_CONFIRMATION':
        ch = input('BOT: Do you want to continue (Y/n) ?')
        if ch == 'y' or ch == 'Y':
            choice = 0
        else:
            choice = 1
        return {'intent-tag': intent['next-intent-tag'][choice]}

    elif action_code == 'ADD_DELIVERY_INSTRUCTIONS':
        instructions = input('Your Instructions: ')
        return {'intent-tag': intent['next-intent-tag'][0]}


def chatbot(message):
    bot_response = ''
    # predict intent tag using trained neural network
    tag = predict_intent_tag(message)
    # get complete intent from intent tag
    intent = get_intent(tag)
    # generate random response from intent
    response = random.choice(intent['responses'])
    bot_response += response

    # check if there's a need to perform some action
    if 'action' in intent.keys():
        action_code = intent['action']
        # perform action
        data = perform_action(action_code, intent)
        # get follow up intent after performing action
        followup_intent = get_intent(data['intent-tag'])
        # generate random response from follow up intent
        response = random.choice(followup_intent['responses'])

        # print randomly selected response
        if len(data.keys()) > 1:
            bot_response += response.format(**data)
        else:
            bot_response += response

    # break loop if intent was goodbye
    if tag == 'goodbye':
        return False

    return bot_response
