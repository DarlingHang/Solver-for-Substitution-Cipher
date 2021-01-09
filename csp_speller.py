import re
import os
import tarfile
from contextlib import closing
from itertools import chain
import pickle

TRY_SUB = 2

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

PATH = os.path.abspath(os.path.dirname(__file__))
DATASET = 'enwiki-20190320-words-frequency.txt'
#DATASET = 'dataset.bz2'
RE = '[A-Za-z]+'
IF_TRAIN = False


class Zero_dict(dict):
    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        try:
            return super(Zero_dict, self).__getitem__(key)
        except KeyError:
            return 0

def cat(*args):
    try:
        return ''.join(args)
    except TypeError:
        return ''.join(chain.from_iterable(args))

class Word(object):
    def __init__(self, word):
        word_ = word.lower()
        slice_range = range(len(word_) + 1)
        slices = []
        for i in range(len(word_) + 1):
            slices.append((word_[:i], word_[i:]))
        self.slices = tuple(slices)
        self.word = word

    def _exchange(self):
        r = []
        for c in ALPHABET:
            for a, b in self.slices[:-1]:
                r.append(cat(a,c,b[1:]))
        return set(r)

    def double_exchange(self):
        r = []
        for a in self._exchange():
            for b in Word(a)._exchange():
                r.append(b)
        
        return set(r)

    def triple_exchange(self):
        r = []
        for a in self.double_exchange():
            for b in Word(a)._exchange():
                r.append(b)
        return set(r)

    def four_exchange(self):
        r = []
        for a in self.triple_exchange():
            for b in Word(a)._exchange():
                r.append(b)
        return set(r)


def count(name):
    if DATASET == "enwiki-20190320-words-frequency.txt":
        dataset = os.path.join(PATH, DATASET)
        counter = {}
        with open(DATASET, "r",encoding='utf-8') as f:
            data = f.readlines()
            for line in data:
                line = line.strip('\n')
                line = line.split()
                counter[line[0]] = line[1]
        return counter
    else:
        dataset = os.path.join(PATH, DATASET)
        tar_path = '{}/{}'.format('words', name)
        with closing(tarfile.open(dataset, 'r:bz2')) as t:
            with closing(t.extractfile(tar_path)) as f:
                counted_words = re.findall(RE, f.read().decode(encoding='utf-8'))
        counter = Zero_dict()
        # Too slow!! should use Zero_dict
        #for word in counted_words:
        #    if word in counter.keys():
        #        counter[word] += 1
        #    else:
        #       counter[word] = 1
        for word in counted_words:
            counter[word] += 1
        return counter
    
if IF_TRAIN:
    if DATASET == "enwiki-20190320-words-frequency.txt":
        COUNTER = count(DATASET)
        COUNTED_WORDS = COUNTER.keys()
        #print(COUNTED_WORDS)
    else:
        COUNTER = count("big.txt")
        COUNTED_WORDS = COUNTER.keys()
    filename = 'counter.pkl'
    f = open(filename, 'wb') 
    pickle.dump(COUNTER, f)
    f.close()  
else:
    filename = os.path.join("model", "counter.pkl")
    with open(filename,'rb') as file:
                COUNTER  = pickle.loads(file.read())
    COUNTED_WORDS = COUNTER.keys()
                
def correct(word):
    """most likely correction for everything up to a double typo"""
    w = Word(word)
    '''try more substitution, but too slow'''
    '''if len(w.word) >= 7:
        candidates = ((w.triple_exchange()&COUNTED_WORDS) or 
                      (w.double_exchange()&COUNTED_WORDS) or 
                      (w._exchange()&COUNTED_WORDS)or [word])
    else:
        candidates = ((w.double_exchange()&COUNTED_WORDS) or 
                      (w._exchange()&COUNTED_WORDS)or [word])'''

    if TRY_SUB == 1:
        candidates = ((w._exchange()&COUNTED_WORDS)or [word]) 
    elif TRY_SUB == 2:
        candidates = ((w.double_exchange()&COUNTED_WORDS) or 
                    (w._exchange()&COUNTED_WORDS)or [word])        
    elif TRY_SUB == 3:
        if len(w.word) >= 7:
            candidates = ((w.triple_exchange()&COUNTED_WORDS) or 
                        (w.double_exchange()&COUNTED_WORDS) or 
                        (w._exchange()&COUNTED_WORDS)or [word])
        else:
            candidates = ((w.double_exchange()&COUNTED_WORDS) or 
                        (w._exchange()&COUNTED_WORDS)or [word])  
    elif TRY_SUB == 4:
        if len(w.word) >= 9:
            candidates = ((w.four_exchange()&COUNTED_WORDS)
                        (w.triple_exchange()&COUNTED_WORDS) or 
                        (w.double_exchange()&COUNTED_WORDS) or 
                        (w._exchange()&COUNTED_WORDS)or [word])

        elif len(w.word) >= 7:
            candidates = ((w.triple_exchange()&COUNTED_WORDS) or 
                        (w.double_exchange()&COUNTED_WORDS) or 
                        (w._exchange()&COUNTED_WORDS)or [word])
        else:
            candidates = ((w.double_exchange()&COUNTED_WORDS) or 
                        (w._exchange()&COUNTED_WORDS)or [word])  
    #print(candidates)
    correction = max(candidates, key=COUNTER.get)
    return correction
