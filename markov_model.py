import numpy as np
import random
import re
import copy 

class Model:
    def __init__(self, bookname, gram_number):
        self.bookname = bookname
        self.gram_number = gram_number
        self.training()
        
    def training(self):
        if self.gram_number == 2:
            print("Start learning with 2-gram LM.")
            with open(self.bookname,'r',encoding='utf-8') as f:
                text = f.read()
            cl = re.compile('[^a-zA-Z]')
            text = cl.sub(' ',text)
            text = text.lower().replace(' ','')
            p1 = {}
            p2 = {}
            
            # p1 = {'a':123, 'b':124}
            for i in text:
                if i not in p1.keys():
                    p1[i] = 1
                else:
                    p1[i] += 1

            # p2 = {'ab': 1243, 'cd': 1345 }
            for i in range(len(text)-1):
                tmp = text[i] + text[i+1]
                if tmp not in p2.keys():
                    p2[tmp] = 1
                else:
                    p2[tmp] += 1
            
            # P(B|A) = number of AB / number of A
            for key in p2.keys():
                tmp = key[0]
                p2[key] /= p1[tmp]
            
            #P(A) = number of A / total number 
            tmp = sum(list(p1.values()))
            for key in p1.keys():
                p1[key] /= tmp
                
            self.p1 = p1
            self.p2 = p2
            print("Learning complete.")

            
        elif self.gram_number == 3:
            print("Start learning with 3-gram LM.")
            with open(self.bookname,'r',encoding='utf-8') as f:
                text = f.read()
            cl = re.compile('[^a-zA-Z]')
            text = cl.sub(' ',text)
            text = text.lower().replace(' ','')
            p1 = {}
            p2 = {}
            p3 = {}
            
            # p1 = {'a':123, 'b':124}
            for i in text:
                if i not in p1.keys():
                    p1[i] = 1
                else:
                    p1[i] += 1

            # p2 = {'ab': 1243, 'cd': 1345 }
            for i in range(len(text)-1):
                tmp = text[i] + text[i+1]
                if tmp not in p2.keys():
                    p2[tmp] = 1
                else:
                    p2[tmp] += 1
            
            # p3 = {'asd':123, 'cvc':123}
            for i in range(len(text)-2):
                tmp = text[i] + text[i+1]+text[i+2]
                if tmp not in p3.keys():
                    p3[tmp] = 1
                else:
                    p3[tmp] += 1    
                    
            # P(C|AB) = number of ABC / number of AB
            for key in p3.keys():
                tmp = key[0] + key[1]
                p3[key] /= p2[tmp]
            
            # P(B|A) = number of AB / number of A
            for key in p2.keys():
                tmp = key[0]
                p2[key] /= p1[tmp]
            
            #P(A) = number of A / total number 
            tmp = sum(list(p1.values()))
            for key in p1.keys():
                p1[key] /= tmp
                
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
            print("Learning complete.")

        elif self.gram_number == 4:
            print("Start learning with 4-gram LM.")
            with open(self.bookname, 'r',encoding='utf-8') as f:
                text = f.read()
            cl = re.compile('[^a-zA-Z]')
            text = cl.sub(' ', text)
            text = text.lower().replace(' ', '')
            p1 = {}
            p2 = {}
            p3 = {}
            p4 = {}

            # p1 = {'a':123, 'b':124}
            for i in text:
                if i not in p1.keys():
                    p1[i] = 1
                else:
                    p1[i] += 1

            # p2 = {'ab': 1243, 'cd': 1345 }
            for i in range(len(text) - 1):
                tmp = text[i] + text[i + 1]
                if tmp not in p2.keys():
                    p2[tmp] = 1
                else:
                    p2[tmp] += 1

            # p3 = {'asd':123, 'cvc':123}
            for i in range(len(text) - 2):
                tmp = text[i] + text[i + 1] + text[i + 2]
                if tmp not in p3.keys():
                    p3[tmp] = 1
                else:
                    p3[tmp] += 1

            for i in range(len(text) - 3):
                tmp = text[i] + text[i + 1] + text[i + 2] + text[i + 3]
                if tmp not in p4.keys():
                    p4[tmp] = 1
                else:
                    p4[tmp] += 1

            #P(D|ABC) = number of ABCD / number of ABC
            for key in p4.keys():
                tmp = key[0] + key[1] + key[2]
                p4[key] /= p3[tmp]

            #P(C|AB) = number of ABC / number of AB
            for key in p3.keys():
                tmp = key[0] + key[1]
                p3[key] /= p2[tmp]

            # P(B|A) = number of AB / number of A
            for key in p2.keys():
                tmp = key[0]
                p2[key] /= p1[tmp]

            # P(A) = number of A / total number
            tmp = sum(list(p1.values()))
            for key in p1.keys():
                p1[key] /= tmp

            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
            self.p4 = p4
            print("Learning complete.")

        elif self.gram_number == 5:
            print("Start learning with 5-gram LM.")
            with open(self.bookname, 'r',encoding='utf-8') as f:
                text = f.read()
            cl = re.compile('[^a-zA-Z]')
            text = cl.sub(' ', text)
            text = text.lower().replace(' ', '')
            p1 = {}
            p2 = {}
            p3 = {}
            p4 = {}
            p5 = {}

            # p1 = {'a':123, 'b':124}
            for i in text:
                if i not in p1.keys():
                    p1[i] = 1
                else:
                    p1[i] += 1

            # p2 = {'ab': 1243, 'cd': 1345 }
            for i in range(len(text) - 1):
                tmp = text[i] + text[i + 1]
                if tmp not in p2.keys():
                    p2[tmp] = 1
                else:
                    p2[tmp] += 1

            # p3 = {'asd':123, 'cvc':123}
            for i in range(len(text) - 2):
                tmp = text[i] + text[i + 1] + text[i + 2]
                if tmp not in p3.keys():
                    p3[tmp] = 1
                else:
                    p3[tmp] += 1

            for i in range(len(text) - 3):
                tmp = text[i] + text[i + 1] + text[i + 2] + text[i + 3]
                if tmp not in p4.keys():
                    p4[tmp] = 1
                else:
                    p4[tmp] += 1

            for i in range(len(text) - 4):
                tmp = text[i] + text[i + 1] + text[i + 2] + text[i + 3] + text[i + 4]
                if tmp not in p5.keys():
                    p5[tmp] = 1
                else:
                    p5[tmp] += 1

            #P(E|ABCD) = number of ABCDE / number of ABCD
            for key in p5.keys():
                tmp = key[0] + key[1] + key[2] + key[3]
                p5[key] /= p4[tmp]

            #P(D|ABC) = number of ABCD / number of ABC
            for key in p4.keys():
                tmp = key[0] + key[1] + key[2]
                p4[key] /= p3[tmp]

            #P(C|AB) = number of ABC / number of AB
            for key in p3.keys():
                tmp = key[0] + key[1]
                p3[key] /= p2[tmp]

            # P(B|A) = number of AB / number of A
            for key in p2.keys():
                tmp = key[0]
                p2[key] /= p1[tmp]

            # P(A) = number of A / total number
            tmp = sum(list(p1.values()))
            for key in p1.keys():
                p1[key] /= tmp

            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
            self.p4 = p4
            self.p5 = p5
            print("Learning complete.")

        elif self.gram_number == 6:
            print("Start learning with 6-gram LM.")
            with open(self.bookname, 'r', encoding='utf-8') as f:
                text = f.read()
            cl = re.compile('[^a-zA-Z]')
            text = cl.sub(' ', text)
            text = text.lower().replace(' ', '')
            p1 = {}
            p2 = {}
            p3 = {}
            p4 = {}
            p5 = {}
            p6 = {}

            # p1 = {'a':123, 'b':124}
            for i in text:
                if i not in p1.keys():
                    p1[i] = 1
                else:
                    p1[i] += 1

            # p2 = {'ab': 1243, 'cd': 1345 }
            for i in range(len(text) - 1):
                tmp = text[i] + text[i + 1]
                if tmp not in p2.keys():
                    p2[tmp] = 1
                else:
                    p2[tmp] += 1

            # p3 = {'asd':123, 'cvc':123}
            for i in range(len(text) - 2):
                tmp = text[i] + text[i + 1] + text[i + 2]
                if tmp not in p3.keys():
                    p3[tmp] = 1
                else:
                    p3[tmp] += 1

            for i in range(len(text) - 3):
                tmp = text[i] + text[i + 1] + text[i + 2] + text[i + 3]
                if tmp not in p4.keys():
                    p4[tmp] = 1
                else:
                    p4[tmp] += 1

            for i in range(len(text) - 4):
                tmp = text[i] + text[i + 1] + text[i + 2] + text[i + 3] + text[i + 4]
                if tmp not in p5.keys():
                    p5[tmp] = 1
                else:
                    p5[tmp] += 1

            for i in range(len(text) - 5):
                tmp = text[i] + text[i + 1] + text[i + 2] + text[i + 3] + text[i + 4] + text[i + 5]
                if tmp not in p6.keys():
                    p6[tmp] = 1
                else:
                    p6[tmp] += 1

            # P(F|ABCDE) = number of ABCDEF / number of ABCDE
            for key in p6.keys():
                tmp = key[0] + key[1] + key[2] + key[3] + key[4]
                p6[key] /= p5[tmp]

            # P(E|ABCD) = number of ABCDE / number of ABCD
            for key in p5.keys():
                tmp = key[0] + key[1] + key[2] + key[3]
                p5[key] /= p4[tmp]

            # P(D|ABC) = number of ABCD / number of ABC
            for key in p4.keys():
                tmp = key[0] + key[1] + key[2]
                p4[key] /= p3[tmp]

            # P(C|AB) = number of ABC / number of AB
            for key in p3.keys():
                tmp = key[0] + key[1]
                p3[key] /= p2[tmp]

            # P(B|A) = number of AB / number of A
            for key in p2.keys():
                tmp = key[0]
                p2[key] /= p1[tmp]

            # P(A) = number of A / total number
            tmp = sum(list(p1.values()))
            for key in p1.keys():
                p1[key] /= tmp

            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
            self.p4 = p4
            self.p5 = p5
            self.p6 = p6
            print("Learning complete.")