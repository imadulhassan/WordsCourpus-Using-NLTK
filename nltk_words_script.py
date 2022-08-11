from openpyxl import Workbook
import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet 
from openpyxl import Workbook
from itertools import * 
import re
from nltk.tokenize import word_tokenize , SyllableTokenizer
import eng_to_ipa as ipa




wb = Workbook()
ws = wb.active
tk = SyllableTokenizer()
ws.append(["WORD", "LEMMA", "ALLWORD", "PART_OF_SPEECH","SYNONYMS","ANTONYMS", "HYPERNIM","DEFINATION","EXX","HOMONYM","EPHOLO","SYLLABLES","PHONETIC"])


wordnetword=[]
for words in wordnet.words():
    wordnetword.append(words)
for word in wordnetword:
    # print(word)
    rword = []
    rword.append(word)
    
    lemmaa = []

    syn = wordnet.synsets(word)[0]
    for lemma in syn.lemmas():
      

        lemmaa.append(lemma.name())
   


    allwords = []
    for ss in wordnet.synsets(word):
        allwords.append(ss.name())

    eallwords =[]
    if len(allwords) > 0: 
        my_stringword = ','.join(allwords)
        # print(my_stringword)
        eallwords.append(my_stringword)
    else:
        eallwords = ["--"]
    # print(allwords)
    pos = []
    asd = []

    synss = wordnet.synsets(word)
    asd.append(set([x.pos() for x in synss]))
    for li in asd:
        for lm in li:
            pos.append(lm)

    epos = []
    if len(pos) > 0:
        my_stringpos = ','.join(pos)
        epos.append(my_stringpos)
        # print(pos)
    else:
        epos = ["--"]


    synonyms = []
    antonyms = []
    hypernyms = []
    #pos = []

    syn = wordnet.synsets(word)[0]
    for lemma in syn.lemmas():
        lemmaa.append(lemma.name())
    # print(lemmaa)
    for syn in wordnet.synsets(word):
        hypernyms.append(syn.name())
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    # print(synonyms)
    # print(antonyms)
    # print(hypernyms)
    esynonyms = []
    if len(synonyms) > 0:
        my_stringsyno = ','.join(synonyms)
        esynonyms.append(my_stringsyno)
    else:
        esynonyms = ["--"]

    eantonyms = []
    if len(antonyms) > 0:
        my_stringanto = ','.join(antonyms)
        eantonyms.append(my_stringanto)

    else:
        eantonyms = ["--"]

    ehypernyms = []
    if len(hypernyms) > 0 :
        my_stringhype = ','.join(hypernyms)
        ehypernyms.append(my_stringhype)
    else:
        ehypernyms = ["--"]



    fdefinition = []
    example = []

    ssyns = wordnet.synsets(word)[0]
    fdefinition.append(ssyns.definition())
    syyns = wordnet.synsets(word)[0]
    example.append(syyns.examples())
    # print(syyns.examples())

    efdefinition = []
    if len(fdefinition) > 0:
        my_stringdefi = ','.join(fdefinition)
        efdefinition.append(my_stringdefi)

    else:
        efdefinition = ["--"]

   


    member_holonymss = []
    part_holonymss = []

    for i,j in enumerate(wordnet.synsets(word)):

        a=wordnet.synset(j.name()).member_holonyms()
        # print(a)
        member_holonymss.append(a)
        # print(member_holonymss)
        b=wordnet.synset(j.name()).part_holonyms()
        # print(b)
        part_holonymss.append(b)
        # print(part_holonymss)
    listToStr1 = ' '.join(map(str, member_holonymss))
    listToStr2 = ' '.join(map(str, part_holonymss)) 
  
    # print(listToStr1)
    # for holo in member_holonymss:
    #     print(holo)
    hoolo=re.findall("\[(.*?)\]", listToStr1)
    hoolo1=re.findall("\[(.*?)\]", listToStr2)

    emholo = []
    if len(member_holonymss) > 0:
        my_stringmholo = ','.join(filter(None,hoolo))
        emholo.append(my_stringmholo)

    else:
        emholo = []
    # print(emholo)

    epholo = []
    if len(part_holonymss) > 0:
        my_stringpholo = ','.join(filter(None,hoolo1))
        epholo.append(my_stringpholo)

    else:
        epholo = []


    syyns = wordnet.synsets(word)[0]
    example.append(syyns.examples())
    # print(example)
    # listToStr = ' '.join([str(elem) for elem in lemmaa])
    # print(listToStr)
    elamma =[]
    my_string = ','.join(lemmaa)
    # print(my_string)
    elamma.append(my_string)
    ex = syyns.examples()
    eex = []
    # print(ex)
    if len(ex) > 0:
        # my_stringex = ','.join(filter(None,ex))
        eex = syyns.examples()
        # eex.append(ex[0])

    else:
        eex = ["--"]
    ra = [1,2,3]
    # print(eex + ra)
    esyllable = []
    syllable = tk.tokenize(word)
    # print(syllable)
    my_stringsyl = '-'.join(syllable)
    esyllable.append(my_stringsyl)

    ephonetics = []

    phone = ipa.convert(word)
    # print(phone)
    my_stringphone = ''.join(phone)
    # print(my_stringphone)
    ephonetics.append(my_stringphone)


    

    for row in zip(rword,elamma,eallwords,epos,esynonyms,eantonyms,ehypernyms,efdefinition,eex,emholo,epholo,esyllable,ephonetics):
        ws.append(row)
        print("Running at word "+row[0])
        wb.save("allwords_s.csv")    

    
