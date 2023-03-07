#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import tensorflow as tf
import json
from memory_profiler import profile

@profile
def load_files(model,tokenizer,test_file):
    new_model = tf.keras.models.load_model(model)
    
    with open(tokenizer) as f:
        data = json.load(f)
        tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)
    
    test_json = open(test_file)
    test_sequence = json.load(test_json)
    
    return new_model,tokenizer,test_sequence


#padding the sequences
@profile
def make_pad(sequences,max_length):
    #takes a sequences and padding them for the nlp model
    data_pad = tf.keras.utils.pad_sequences(sequences, maxlen=max_length,padding="post",truncating="post")
    
    return data_pad

@profile
def main_func():
    
    model,tokenizer,test_sequence = load_files('my_model','tokenizer_json.json','recipe.json')
    
    for k, v in test_sequence.items():
    
        test_sequences = tokenizer.texts_to_sequences(v)
        test_padded = make_pad(test_sequences,55)
        prediction = model.predict(test_padded)
        if sum(prediction) < 0.5:
            print(k, 'prediction: ', sum(prediction), " labeld as Recipe")
        else:
            print(k, 'prediction: ', sum(prediction), " labeld as instructions")
        print()


if __name__ == "__main__":
    main_func()
    

