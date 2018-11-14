
import newspaper 
import spacy
import wikipedia
import pymongo
import pprint

myclient = pymongo.MongoClient('mongodb+srv://psachaj:jump100!@eecs338localangle-toryj.mongodb.net/test?retryWrites=true')
mydb = myclient['mydatabase']
articles = mydb["info"]


# Python code to remove duplicate elements 
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 


cnn = newspaper.build('http://www.cnn.com', memoize_articles = False)
"""
bbc = newspaper.build('http://www.bbc.com', memoize_articles = False)
forbes = newspaper.build('http://www.forbes.com', memoize_articles = False)
nytimes = newspaper.build('http://www.nytimes.com', memoize_articles = False)
wsj = newspaper.build('http://www.wsj.com', memoize_articles = False)
washpost = newspaper.build('http://www.washingtonpost.com', memoize_articles = False)
econ = newspaper.build('http://www.economist.com', memoize_articles = False)
newyork = newspaper.build('http://www.newyorker.com', memoize_articles = False)
atlantic = newspaper.build('http://www.the atlantic.com', memoize_articles = False)
usatoday = newspaper.build('https://www.usatoday.com/news/', memoize_articles = False)
nbc = newspaper.build('https://www.nbcnews.com/', memoize_articles = False)
abc = newspaper.build('https://abcnews.go.com/', memoize_articles = False)
bi = newspaper.build('https://www.businessinsider.com/', memoize_articles = False)
cbs = newspaper.build('https://www.cbsnews.com/', memoize_articles = False)
"""


allsources = cnn.articles 
"""
+ bbc.articles + forbes.articles + nytimes.articles + wsj.articles + washpost.articles + econ.articles + newyork.articles + atlantic.articles + usatoday.articles + nbc.articles + abc.articles + bi.articles + cbs.articles
"""
alltexts = allsources

urls = list()

for article in allsources:
    urls.append(article.url)


print(len(allsources))

totaldict = []

currfortotal = 1


from newspaper import fulltext
import requests
spacyreader = spacy.load('en')

for i in range(1, 5):
    try:
        html = requests.get(allsources[i].url).text
        text = fulltext(html)
        alltexts[i] = text
        doc = spacyreader(alltexts[i])
        defaultdict = {}
        defaultdict["url"] = ""
        defaultdict["tags"] = []
        defaultdict["url"] = urls[i]
        searchedlist = list()
        for ent in doc.ents:
            if ent.label_ == 'GPE':
                defaultdict["tags"] += [ent.text]
            if (ent.label_ == 'PERSON' or ent.label_ == 'ORG'):
                if not (ent.text in searchedlist):
                    try:
                        searchedlist.append(ent.text)
                        wiki_summary = wikipedia.summary(ent.text)
                        doc_wiki = spacyreader(wiki_summary)
                        for ent in doc_wiki.ents:
                            if ent.label_ == 'GPE':
                                defaultdict["tags"] += [ent.text]
                    except:
                        searchedlist.append(ent.text)
        defaultdict["tags"] = list(set(defaultdict["tags"]))
        totaldict.insert(currfortotal, defaultdict)
        currfortotal += 1
        del defaultdict
        print(i)
    except:
        alltexts[i] = "Error"
 

for a in totaldict:
    articles.insert_one(a)

x = articles.find({"tags": { "$elemMatch": { "$eq": "Washington" } }})

for y in x:
    print(y['url'])
    
myclient.close()       
        

    
    










#cnn_first.download()
#cnn_first.parse()
#print(cnn_first.text)
#cnn_first.nlp()
#print(cnn_first.keywords)
#print(cnn_first.authors)
#print(cnn_first.summary)
#print(cnn_first.text)
#print(cnn_first.text)





"""
from newspaper import fulltext
import requests
html = requests.get(cnn_first.url).text
text = fulltext(html)
print(text)





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


nlp = spacy.load('en')
doc = nlp('Steve Jobs and Google is looking at buying U.K. startup for $1 billion')
#doc = nlp(cnn_first.text)
#for token in doc:
#    print(token.text)
    
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    


wiki_summary = wikipedia.summary("google")
#print(wiki_summary.text, wiki_summary.label)

doc_wiki = nlp(wiki_summary)
for ent in doc_wiki.ents:
    if ent.label_ == 'GPE':
        print(ent.text)
        """