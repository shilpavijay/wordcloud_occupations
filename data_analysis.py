import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import csv

# df = pd.read_csv('Adult_data/adult.csv')

ms_words = ''
stopwords = set(STOPWORDS)

with open('Adult_data/adult.data') as file:
    read = csv.DictReader(file)
    for eachline in read:
        data = dict(eachline)
        ms = str(data.get('OCCUPATION'))  # typecast

        # not required if a single word. Keeping here for fields like comments which have a line of different words
        # tokens = ms.split()
        # for i in range(len(tokens)):  #if multiple words in the field
        #     tokens[i] = tokens[i].lower()

        # ms_words += ''.join(tokens)+''  # work with multiple words
        ms_words += ms


wordcloud = WordCloud(width=800, height=800,
                      stopwords=stopwords, min_font_size=10).generate(ms_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
