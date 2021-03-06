from sklearn.linear_model import LogisticRegression

import nltk
nltk.download("wordnet")
nltk.download("omw")
import re
from collections import Counter
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import numpy as np
import pickle
from collections import defaultdict
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.ensemble import ExtraTreesRegressor
from nltk.corpus import wordnet 
from nltk.corpus import wordnet as wn
import spacy
import en_core_web_sm
import es_core_news_sm
from sklearn.neighbors import KNeighborsRegressor

class Baseline(object):

    def __init__(self, language):
        self.language = language
        self.dictionary = defaultdict(int)

        self.spanish_stop_words = [" un",	" una",	" unas",	" unos",	" uno",	" sobre",	" todo",	" también",	" tras",	" otro",	" algún",	" alguno",	" alguna",	" algunos",	" algunas",	" ser",	" es",	" soy",	" eres",	" somos",	" sois",	" estoy",	" esta",	" estamos",	" estais",	" estan",	" como",	" en",	" para",	" atras",	" porque",	" por qué",	" estado",	" estaba",	" ante",	" antes",	" siendo",	" ambos",	" pero",	" por",	" poder",	" puede",	" puedo",	" podemos",	" podeis",	" pueden",	" fui",	" fue",	" fuimos",	" fueron",	" hacer",	" hago",	" hace",	" hacemos",	" haceis",	" hacen",	" cada",	" fin",	" incluso",	" primero",
                      " desde",	" conseguir",	" consigo",	" consigue",	" consigues",	" conseguimos",	" consiguen",	" ir",	" voy",	" va",	" vamos",	" vais",	" van",	" vaya",	" gueno",	" ha",	" tener",
                      " tengo",	" tiene",	" tenemos",	" teneis",	" tienen",	" el",	" la",	" lo",	" las",	" los",	" su",	" aqui",	" mio",	" tuyo",
                      " ellos",	" ellas",	" nos",	" nosotros",	" vosotros",	" vosotras",	" si",	" dentro",	" solo",	" solamente",	" saber",
                      " sabes",	" sabe",	" sabemos",	" sabeis",	" saben",	" ultimo",	" largo",	" bastante",	" haces",
                      " muchos",	" aquellos",	" aquellas",	" sus",	" entonces",	" tiempo",	" verdad",	" verdadero",	" verdadera",
                      " cierto",	" ciertos",	" cierta",	" ciertas",	" intentar",	" intento",	" intenta",	" intentas",	" intentamos",
                      " intentais",	" intentan",	" dos",	" bajo",	" arriba",	" encima",	" usar",	" uso",
                      " usas",	" usa",	" usamos",	" usais",	" usan",	" emplear",	" empleo",	" empleas",	" emplean",
                      " ampleamos",	" empleais",	" valor",	" muy",	" era",	" eras",	" eramos",	" eran",	" modo",
                      " bien",	" cual",	" cuando",	" donde",	" mientras",	" quien",	" con",	" entre",	" sin",
                      " trabajo",	" trabajar",	" trabajas",	" trabaja",	" trabajamos",	" trabajais",	" trabajan",
                      " podria",	" podrias",	" podriamos",	" podrian",	" podriais",	" yo",	" aquel"]

        self.english_stop_words = ["i","me","my","myself","we","our",    "ours",	"ourselves",	"you",	"your",	"yours",	"yourself",	"yourselves",	"he",	"him",	"his",	"himself",	"she",	"her",	"hers",	"herself",
                      "it",	"its",	"itself",	"they",	"them",	"their",	"theirs",	"themselves",	"what",	"which",	"who",	"whom",	"this",
                      "that",	"these",	"those",	"am",	"is",	"are",	"was",	"were",	"be",	"been",	"being",	"have",	"has",	"had",	"having",
                      "do",	"does",	"did",	"doing",	"a",	"an",	"the",	"and",	"but",	"if",	"or",	"because",	"as",	"until",	"while",
                      "of",	"at",	"by",	"for",	"with",	"about",	"against",	"between",	"into",	"through",	"during",	"before",
                      "after",	"above",	"below",	"to",	"from",	"up",	"down",	"in",	"out",	"on",	"off",	"over",	"under",	"again",
                      "further",	"then",	"once",	"here",	"there",	"when",	"where",	"why",	"how",	"all",	"any",	"both",	"each",	"few",	"more",
                      "most",	"other",	"some",	"such",	"no",	"nor",	"not",	"only",	"own",	"same",	"so",	"than",	"too",	"very",	"s",	"t",	"can",
                      "will",	"just",	"don",	"should",	"now"]

        # from 'Multilingual and Cross-Lingual Complex Word Identification' (Yimam et. al, 2017)
        if language == 'english':
            self.avg_word_length = 5.3
            self.dictionary = pickle.load(open('English-model.pkl',"rb"))           
        else:  # spanish
            self.avg_word_length = 6.2
            self.dictionary = pickle.load(open('Spanish-model.pkl',"rb"))

        self.model = LogisticRegression()
        #self.param_dist = {
        # 'n_estimators': [50, 100],
        # 'learning_rate' : [0.01,0.05,0.1,0.3,1],
        # 'loss' : ['linear', 'square', 'exponential']
        # }
        #self.param_distribs = {
        #'n_neighbors': [2,6,5,10],
        #'weights': ['uniform','distance']
       # }

        #self.model = KNeighborsRegressor()
       # self.grid = GridSearchCV(self.model, self.param_distribs , cv=10)


        #self.parameters = [
            #  {'C': [1, 10, 100], 'kernel': ['linear']},
            #  {'C': [1, 10, 100], 'gamma': [0.1,0.001, 0.0001], 'kernel': ['rbf','sigmoid','poly']},
            # ]
        #self.clf = GridSearchCV(svm.SVR(), self.parameters)
       # self.rnd_search= RandomizedSearchCV(AdaBoostRegressor(random_state=42),param_distributions = self.param_dist,cv=3,n_iter = 20,n_jobs=-1,random_state=42)
        #self.model = DecisionTreeRegressor()
        # Decision Tree Hyperperemeters Range for optimization
        #self.param_distribs = {
           #'min_samples_split': randint(low=2, high=10),
           #'min_samples_leaf': randint(low=50, high=200),
           # 'n_estimators': [50, 100]
          # }
        #self.model= RandomForestRegressor(random_state=42)
        #self.model = DecisionTreeRegressor(random_state=42)
        #self.model = ExtraTreesRegressor(random_state=43)
        #self.rnd_search = RandomizedSearchCV(self.model, param_distributions=self.param_distribs,
        #                    n_iter=15,cv=5, scoring='neg_mean_squared_error', random_state=42)
        #print(self.rnd_search)


    def consonant_sum(self,word):
        consonants = list("bcdfghjklmnpqrstvexz")
        number_of_consonants = sum(word.count(c) for c in consonants)
        return number_of_consonants

    def vowel_sum(self,word):
        #https://stackoverflow.com/questions/7736211/python-counting-the-amount-of-vowels-or-consonants-in-a-user-input-word
        vowels = list("aeiouy")
        number_of_vowels = sum(word.count(c) for c in vowels)
        return number_of_vowels
        

    def is_stopword(self,word):
        check  = 0
        if self.language == 'Emglish':
            if word in self.english_stop_words:
                check=1
        else:
            if word in self.spanish_stop_words:
                check=1
        return check
                
    def is_nounphrase(self,word):
        if len(word.split(" ")) > 1:
            return 1
        else:
            return 0

    def extract_features(self, word,sent):
        len_chars = len(word) / self.avg_word_length
        len_tokens = len(word.split(' '))
        senses = len(wn.synsets(word))
        sylable = self.syllables(word)
        consonant_sums = self.consonant_sum(word)
        vowel_sums = self.vowel_sum(word)
        self.unigram_probability(sent)
        unigram_prob = self.get_unigram_prob(self.dictionary,word)
        stop_word = self.is_stopword(word)
        noun  = self.is_nounphrase(word)
        syn_count,syn_count2 = self.synonyms_hypernyms(word)
        #Counter(re.sub("[^\w']"," ",sent).split())
        #x = str(len_chars)+ ',' + str(len_tokens) + ',' + str(senses) + ',' + str(sylable)
        return [str(len_chars),str(len_tokens),str(senses),str(sylable)]#,str(unigram_prob), str(vowel_sums) ,str(consonant_sums),str(stop_word),str(noun),str(syn_count),str(syn_count2)]#,str(unigram_prob) ,str(stop_word),str(noun),str(syn_count),str(syn_count2)]
    

    def synonyms_hypernyms(self,word):
        count=0
        temp= word.split(" ")
        count2 = 0
        if self.language == "english":
            if len(word.split(" ")) > 1:
                for wd in temp:
                    count+=  len(wordnet.synsets(wd, lang='eng'))
                    for synset in wordnet.synsets(wd, lang='eng'):
                        count2+= len(synset.hypernyms())
            else:
                count+= len(wordnet.synsets(word, lang='eng'))
                for synset in wordnet.synsets(word, lang='eng'):
                    count2+= len(synset.hypernyms())
            count = count/len(temp)
            count2 = count2/len(temp)
        else:
            if len(word.split(" ")) > 1:
                for wd in temp:
                    count+=  len(wordnet.synsets(wd, lang='spa'))
                    for synset in wordnet.synsets(wd, lang='spa'):
                        count2+= len(synset.hypernyms())
            else:                
                count+= len(wordnet.synsets(word, lang='spa'))
                for synset in wordnet.synsets(word, lang='spa'):
                        count2+= len(synset.hypernyms())
            count = count/len(temp)
            count2 = count2/len(temp)
        return (round(count),round(count2))

    def syllables(self,word):
        #referred from stackoverflow.com/questions/14541303/count-the-number-of-syllables-in-a-word
        count = 0
        vowels = 'aeiouy'
        word = word.lower()
        if word[0] in vowels:
            count +=1
        for index in range(1,len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count +=1
        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count+=1
        if count == 0:
            count +=1
        return count

    def unigram_probability(self,sent):
        total_word_count = len(self.dictionary.keys())
        for word in re.findall(r"[\w']+",sent['target_word'].lower()): #
            if word in self.dictionary:  
                total_word_count+=1
                self.dictionary[word]+=1/total_word_count             
            else:
                total_word_count+=1
                self.dictionary[word] = 0
        return 0

        
            
                    
    def get_unigram_prob(self,dictionary,target_word):
        return dictionary[target_word]        
        
    def train(self, trainset):
        X = []
        y = []
        sentences = []
        bigrams = []


        for sent in trainset:
            X.append(self.extract_features(sent['target_word'],sent))
            y.append([sent['gold_label']]) #for logistic regressipon
            #y.append([float(sent['gold_label'])])

        #y = np.asarray(y, dtype=float)
        #y = y.ravel()
       # self.model.fit(np.array(X,object),np.array(pd.DataFrame(y,columns=['Gold_Labels']).values.ravel(),object))
        self.model.fit(np.array(X,object),np.array(pd.DataFrame(y,columns=['Gold_Labels']).values.ravel(),object))
        #print('Preparing Data')
       # self.grid.fit(np.array(X), y)
        #self.grid.fit(np.array(X,object),np.array(pd.DataFrame(y,columns=['Gold_Labels']).values.ravel(),object))
        #print('Best Estimator')
        #print(self.grid.best_estimator_)
        #print('Best Parmeter')
       # print(self.grid.best_params_)
        #print(len(X))
        #print(len(y))
       # self.model.fit(np.array(X,object),np.array(pd.DataFrame(y,columns=['Gold_Labels']).values.ravel(),object))
        #self.clf.fit(np.array(X,object),np.array(pd.DataFrame(y,columns=['Gold_Labels']).values.ravel(),object))
        #print('Best Estimator')
        ##print(self.clf.best_estimator_)
        #print('Best Parameter')
        #print(self.clf.best_params_)
        #self.rnd_search.fit(np.array(X,object),np.array(pd.DataFrame(y,columns=['Gold_Labels']).values.ravel(),object))
        #print(self.rnd_search.cv_results_)
        #print(self.rnd_search.best_estimator_)
        #print(self.rnd_search.best_params_)
       
        

    def test(self, testset,gold_labels):
        X = []
        i=0
        R=[]
        for sent in testset:
            X.append(self.extract_features(sent['target_word'],sent))
            #if self.model.predict(np.array(self.extract_features(sent['target_word'],sent),object))[0] != gold_labels[i]:
                #R.append(sent['target_word'])
          
            #i+=1
      
        #print(R)
        return self.model.predict(np.array(X,object)) #self.rnd_search.predict(X).round() #self.model.predict(np.array(X,object)) #self.clf.predict(X).round() #self.rnd_search.predict(X).round() #self.model.predict(np.array(X,object)) #self.grid.predict(X).round()
