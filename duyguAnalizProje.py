#gerekli kütüphaneleri import ettim.
from re import split
from urllib.request import build_opener
import nltk
from nltk.util import pr

nltk.download('punkt')
nltk.download('stopwords')

#from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from nltk.stem import snowball
from snowballstemmer import TurkishStemmer

import pandas as pd

#excel formatı ile bütün cümleler okundu.
dc=pd.read_excel("/Users/123/Desktop/3-1/python/ornekCumleler.xlsx")
dm=pd.read_excel("/Users/123/Desktop/3-1/python/kelime.xlsx")
all_stem_lists3 = []
all_stem_lists4 = []
dm=dm.astype(str)
dc=dc.astype(str)

a=dm["olumsuz isim&sıfat"] #a değişkenine exceldeki "olumsuz isim&sıfat" sütununu atadım.
b=dm["olumsuz fiil"] #b değişkenine exceldeki "olumsuz fiil" sütununu atadım.

for b in dm:
    #burada iç içe döngü kuraraktan sütundaki bütün kelimeleri ilk küçülttüm sonra da stemmer kütüphanesini
    #kullanıp köklerini aldım.
    for c in dm["olumsuz fiil"]:
            
            c=c.lower()
            bune2 = word_tokenize(c)

            stopWords = set(stopwords.words('turkish'))
            wordsU=[]

            for w in bune2:
                if w not in stopWords:
                        wordsU.append(w)

            ps =TurkishStemmer()
            for w in wordsU:
                rootWord=ps.stemWord(w)
                all_stem_lists3.append(rootWord)

#olumsuz listesi tekrar eden kelimelerden arındırdım.
newlist3 = sorted(set(all_stem_lists3), key=lambda x:all_stem_lists3.index(x))

for b in dm:
    
    for c in dm["olumsuz isim&sıfat"]:
            
            c=c.lower()
            bune2 = word_tokenize(c)

            stopWords = set(stopwords.words('turkish'))
            wordsU=[]

            for w in bune2:
                if w not in stopWords:
                        wordsU.append(w)

            ps =TurkishStemmer()
            for w in wordsU:
                rootWord=ps.stemWord(w)
                all_stem_lists4.append(rootWord)

#olumsuz listesi tekrar eden kelimelerden arındırıldı.
newlist5= sorted(set(all_stem_lists4), key=lambda x:all_stem_lists4.index(x))

newlist7=newlist3+newlist5

all_stem_lists4 = []
for b in dm:
    
    for c in dm["olumlu isim&sıfat"]:
            
        c=c.lower()
            
        bune2 = word_tokenize(c)

        stopWords = set(stopwords.words('turkish'))
        wordsU=[]

        for w in bune2:
            if w not in stopWords:
                    wordsU.append(w)
   
        ps =TurkishStemmer()
        for w in wordsU:
            rootWord=ps.stemWord(w)
            all_stem_lists4.append(rootWord)

newlist2 = sorted(set(all_stem_lists4), key=lambda x:all_stem_lists4.index(x))

all_stem_lists6 = []
for b in dm:
    
    for c in dm["olumlu fiil"]:
            
        c=c.lower()
            
        bune2 = word_tokenize(c)

        stopWords = set(stopwords.words('turkish'))
        wordsU=[]

        for w in bune2:
            if w not in stopWords:
                    wordsU.append(w)
        
        ps =TurkishStemmer()
        for w in wordsU:
            rootWord=ps.stemWord(w)
            all_stem_lists6.append(rootWord)

newlist6 = sorted(set(all_stem_lists6), key=lambda x:all_stem_lists6.index(x))

newlist8=newlist6+newlist2

all_stem_lists = []

print("-----------------------------------------")

for x in dc:
    
    for y in dc[x]:
        bune=sent_tokenize(y)
        #cümlelerden noktalama işaretleri silinir.
        mypunc= [".",":",";", ",", "!", "?", "\"","\'","<",">"]
        for chk in y:
            if chk in mypunc:
                y = y.replace(chk, "")
        #bütün kelimeler küçük harfe çevrilir.
        y=y.lower()

        #kelimelere ayırdım.
        bune2 = word_tokenize(y)
        
        stopWords = set(stopwords.words('turkish'))
        wordsU=[]

        for w in bune2:
            if w not in stopWords:
                wordsU.append(w)
        #köklerini buldum.
        ps =TurkishStemmer()
        for w in wordsU:
            rootWord=ps.stemWord(w)
            all_stem_lists.append(rootWord)
        #buraya kadar bütün metinler kök haline indirildi ve bağlaç-edatlar silindi.
       
#newlist, listedeki aynı köke sahip cümleleri siler ve unique hale getirdim.
newlist = sorted(set(all_stem_lists), key=lambda x:all_stem_lists.index(x))

print("-----------------------------------------")

sayacOlumlu=0
sayacNotr=0
sayacOlumsuz=0

#olumlular için sayaç döngüsü kurdum.

for z in newlist:
    for n in newlist8:
            if (n == z ):    
                sayacOlumlu=sayacOlumlu+1

#olumsuzlar için sayaç döngüsü kurdum.
for z in newlist:
    for n in newlist7:
            if (n == z ):    
                sayacOlumsuz=sayacOlumsuz+1
            
print("olumlu yakalama sayısı:",sayacOlumlu, "/" , len(dc)*3)
print("nötr yakalama sayısı:",(len(dc)*3-(sayacOlumlu+sayacOlumsuz)),"/",len(dc)*3)
print("olumsuz yakalama sayısı:",sayacOlumsuz,"/",len(dc)*3)