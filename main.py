import nltk
import os
from nltk.corpus import stopwords
from textblob import TextBlob
import spacy
nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Tokenization
    tokens = nltk.word_tokenize(text)
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
    
    # Lemmatization
    lemmatized_tokens = [nlp(word)[0].lemma_ for word in filtered_tokens]
    
    return " ".join(lemmatized_tokens)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    
    return sentiment_score


for i in range(1, 6):
    with open(f"./noticias/newNetflix{i}.txt", "r", encoding='UTF8') as file:
        file_content = file.read()
    
    print(f"netflix{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")
    with open(f"./stats/newnetflix.txt", "a+") as file:
        file.write(f"netflix{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")


"""
for i in range(1, 8):
    with open(f"./noticias/EA{i}.txt", "r") as file:
        file_content = file.read()

    print(f"EA{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")
    with open(f"./stats/EA.txt", "a+") as file:
        file.write(f"EA{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")

for i in range(1, 9):
    with open(f"./noticias/netflix{i}.txt", "r") as file:
        file_content = file.read()
    
    print(f"netflix{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")
    with open(f"./stats/netflix.txt", "a+") as file:
        file.write(f"netflix{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")

for i in range(1, 10):
    with open(f"./noticias/tencent{i}.txt", "r") as file:
        file_content = file.read()
    
    print(f"tencent{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")
    with open(f"./stats/tencent.txt", "a+") as file:
        file.write(f"tencent{i}:\n{analyze_sentiment(file_content)}\n{analyze_sentiment(preprocess_text(file_content))}\n")

"""