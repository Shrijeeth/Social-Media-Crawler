import tensorflow as tf
import json

def load_model() :
    model = tf.keras.models.load_model('model/model.h5')
    stem = True
    preprocess = True
    maxlen = 250
    return model,stem,preprocess,maxlen

def get_tokenizer() :
    with open('model/tokenizer.json') as f:
        js = json.load(f)
        tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(js)
    return tokenizer

def get_word_array(content,maxlength) :
    tokenizer = get_tokenizer()
    sequences = tokenizer.texts_to_sequences([content])
    word_array = tf.keras.preprocessing.sequence.pad_sequences(sequences,maxlen=maxlength,padding='post')
    return word_array