from markov_model import Model
import pickle
import os

filename = 'model_from_wap.pkl'
model_from_wap = Model('war_and_peace.txt', 6)
f = open(filename, 'wb') 
pickle.dump(model_from_wap, f)
f.close()  