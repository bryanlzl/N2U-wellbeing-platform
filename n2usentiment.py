import nltk
import nltk.tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import matplotlib.pyplot as plt
from collections import Counter

def sentimentanalysis(text):
    text=text.lower()
    text=text.replace("\n","")
    text=text.translate(str.maketrans("","",string.punctuation))
    tokenize_words=word_tokenize(text)
    clean_words=[]
    for i in tokenize_words:
        if i not in stopwords.words("english"):
            clean_words.append(i)
    emotions=[]
    with open("emotion.txt","r") as file:
        for i in file:
            text1=i.replace("\n","")
            text1=text1.strip()
            text1=text1.replace(" ","")
            text1=text1.replace(",","")
            text1=text1.replace("'","")
            word,emotion=text1.split(":")
            if word in clean_words:
                emotions.append(emotion)

    return [SentimentIntensityAnalyzer().polarity_scores(text), Counter(emotions)]