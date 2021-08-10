import codecs
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
import re

index_num = 0

# NLTK's default Russian stopwords
default_stopwords = set(nltk.corpus.stopwords.words('russian'))

input_files = ['poems_no_dates_1.txt', 'poems_no_dates_2.txt']

for f in input_files:
    fp = codecs.open(f, 'r', 'utf-8')


    t = fp.read()

    new_lines = []

    lines_split = LineTokenizer(blanklines='discard').tokenize(t)

    for line in lines_split:
        words = nltk.word_tokenize(line)

        words = [word.lower() for word in words]

        # Remove single character words/punctuation
        words = [word for word in words if len(word) > 1]

        # Remove numbers
        words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
        words = [word.lower() for word in words]

        # Remove stopwords
        words = [word for word in words if word not in default_stopwords]

        for word in words:
            word = [item.replace("_", "") for item in word]
            word = [item.replace("|", "") for item in word]
            pattern = '[0-9]'
            word = [re.sub(pattern, '', i) for i in word]
            word = [item.replace("'", "") for item in word]
            word = [item.replace("[", "") for item in word]
            word = [item.replace("]", "") for item in word]

        str_words = " ".join(words)
        new_lines.append(str_words)


        print(line)

    with open(('lines_' + input_files[index_num]), 'w') as f:
            for item in new_lines:
                    f.write("\n" + (str(item)))

    index_num += 1
