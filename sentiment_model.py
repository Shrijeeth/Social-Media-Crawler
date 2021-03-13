import tensorflow as tf

def load_model1() :
    model = tf.keras.models.load_model('model1')
    return model
