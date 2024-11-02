from flair.models import SequenceTagger,TextClassifier
from flair.data import Sentence
from flair.nn import Classifier
from flair.embeddings import WordEmbeddings , DocumentPoolEmbeddings

# t = Classifier.load('ner-ontonotes-large')
# t = Classifier.load('ner')
# t = Classifier.load('ner-large')
#
# # making a sentence
# s = Sentence("On September 1st George won 1 dollar while watching Game of Thrones.. ")
#
# #loading the sentence
# # t = Classifier.load('ner-ontonotes-large')
# t.predict(s)
#
# print(s)


# s = Sentence('I Love My Country...')
#
# t = Classifier.load('sentiment')
#
# t.predict(s)
#
# print(s)


# tagger = SequenceTagger.load('ner')
#
# sentence = Sentence("Barack Obama was the 44th president of the United States.")
#
# tagger.predict(sentence)
#
# print(sentence.to_tagged_string())



# cla = TextClassifier.load('sentiment')
#
# s = Sentence("hello! how are you ??")
#
# cla.predict(s)
#
# print(s)

glo = WordEmbeddings("glove")

doc = DocumentPoolEmbeddings(glo)

sen = Sentence("hello !!! how are u ???")

doc.embed(sen)

print(sen.get_embedding())