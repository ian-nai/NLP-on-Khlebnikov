import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
import re
from compress_pickle import dump, load

index_num = 0


# Note: creating this many pickle files at once will be very slow
files = ['lines_poems_no_dates_1.txt', 'lines_poems_no_dates_2.txt']

nlp = spacy.load("ru_core_news_lg")


for f in files:
    with open(f) as file:
        text_data = file.read()


    doc = nlp(text_data)


    fname1 = ("nlp_" + (files[index_num]) + ".pkl")
    fname2 = ("nlp_" + (files[index_num]) + ".gz")

    dump(doc,fname1)
    dump(doc, fname2)

    index_num += 1
