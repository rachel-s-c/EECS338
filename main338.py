# -*- coding: utf-8 -*-


import newspaper 

cnn = newspaper.build('http://www.cnn.com')

#for article in bbc.articles:
#    print(article.url)
#    print(article.authors)
#    print(article.keywords)


cnn_first = cnn.articles[0]
cnn_first.download()
cnn_first.parse()
cnn_first.nlp()
print(cnn_first.keywords)
print(cnn_first.authors)
print(cnn_first.summary)

"""

from newspaper import Article
url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)
article.download()
article.parse()
article.nlp()
print(article.keywords)
print(article.authors)
print(article.summary)
"""


