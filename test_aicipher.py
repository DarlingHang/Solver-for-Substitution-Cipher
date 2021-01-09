import ai_cipher
import numpy as np
import pickle
import matplotlib.pyplot as plt
import os

message = '''But here is an artist. He desires to paint you the dreamiest, shadiest,
quietest, most enchanting bit of romantic landscape in all the valley
of the Saco. What is the chief element he employs? There stand his
trees, each with a hollow trunk, as if a hermit and a crucifix were
within; and here sleeps his meadow, and there sleep his cattle; and up
from yonder cottage goes a sleepy smoke. Deep into distant woodlands
winds a mazy way, reaching to overlapping spurs of mountains bathed in
their hill-side blue.  '''

with open(os.path.join("model","model_from_wap.pkl"),'rb') as file:
                model_from_wap  = pickle.loads(file.read())
#print(model_from_wap.p2.keys())
a = ai_cipher.Cipher(message=message, bookname = None, gram_number = 3,
                     whether_blank = True, whether_speller = True, 
                     pretrained_model=model_from_wap)
ser = []
for i in range(100):
    a.run()
    ser.append(a.SER)
y = ser
x = np.arange(100)
plt.scatter(x,y,marker=',')
plt.show()

