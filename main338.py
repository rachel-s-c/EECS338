# -*- coding: utf-8 -*-


import newspaper 
import spacy
import wikipedia 


cnn = newspaper.build('http://www.cnn.com', memoize_articles = False)
bbc = newspaper.build('http://www.bbc.com', memoize_articles = False)
cnn_first = cnn.articles[10]
cnn_first.download()
cnn_first.parse()
#print(cnn_first.text)
#cnn_first.nlp()
#print(cnn_first.keywords)
#print(cnn_first.authors)
#print(cnn_first.summary)
#print(cnn_first.text)
#print(cnn_first.text)
#print(cnn_first.url)




"""
from newspaper import fulltext
import requests

html = requests.get(cnn_first.url).text
text = fulltext(html)
print(text)

"""



"""
from newspaper import Article
url = 'https://www.cnn.com/2018/10/23/europe/eu-italy-budget-intl/index.html'
article = Article(url)
article.download()
article.parse()
#article.nlp()
#print(article.keywords)
#print(article.authors)
#print(article.summary)
print(article.text)
"""

nlp = spacy.load('en')
#doc = nlp('Steve Jobs Apple is looking at buying U.K. startup for $1 billion')
doc = nlp(cnn_first.text)
#for token in doc:
#    print(token.text)
    
#for ent in doc.ents:
#    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    

wiki_summary = wikipedia.summary("google")
#print(wiki_summary.text, wiki_summary.label)

doc_wiki = nlp(wiki_summary)
for ent in doc_wiki.ents:
    if ent.label_ == 'GPE':
        print(ent.text)
 
