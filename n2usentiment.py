import nltk
import nltk.tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import matplotlib.pyplot as plt
from collections import Counter

def sentimentanalysis(text):
    cleaned_list, emotion_list = [], []
    text = text.lower()
    text = text.replace("\n", "")
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokenize_words = word_tokenize(text)
    for i in tokenize_words:
        if i not in stopwords.words("english"):
            cleaned_list.append(i)
    with open("emotion.txt", "r") as file:
        for words in file:
            keyword = words.replace("\n", "")
            keyword = keyword.strip()
            keyword = keyword.replace(" ", "")
            keyword = keyword.replace(",", "")
            keyword = keyword.replace("'", "")
            word, emotion = keyword.split(":")
            if word in cleaned_list:
                emotion_list.append(emotion)
    return [SentimentIntensityAnalyzer().polarity_scores(text), Counter(emotion_list)]
