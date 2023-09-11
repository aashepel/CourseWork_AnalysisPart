import json
import re
import spacy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.probability import FreqDist

file = open("C:\\Users\\Alexandr\\Downloads\\messagesOfPosts.json", 'r', encoding='utf-8-sig')
fileText: str = file.read()


messagesAsJson = json.loads(fileText)

messages = []

for message in messagesAsJson:
    messages.append(message["Message"])

allMessagesInString = " ".join(messages)
allMessagesInString = allMessagesInString.replace('\n', ' ')
allMessagesInString = re.sub("\s\s+", " ", allMessagesInString)

nlp = spacy.load("ru_core_news_lg")

doc = nlp(allMessagesInString)

tokens = []
for token in doc:
    if not token.is_stop and not token.is_punct and not any(ch.isdigit() for ch in token.text):
        tokens.append(token.lemma_)

tokensInString = " ".join(tokens)

cloud = WordCloud(max_words=50, width=1600, height=1200, min_font_size=14).generate(tokensInString)

fig = plt.figure(figsize=(8, 6), dpi=200)

plt.imshow(cloud)
plt.axis('off')

plt.show()

fdist = FreqDist(tokens)
top50 = fdist.most_common(50)

for element in top50:
    print(f"{element[0]} : {element[1]}")