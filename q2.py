from nltk.corpus import wordnet as wn
import loader

for v in loader.dev_instances.itervalues():
    print v
    #print wn.synsets(v.lemma)

