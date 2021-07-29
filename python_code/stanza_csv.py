import stanza
from collections import Counter
import csv
from nltk.tokenize import LineTokenizer

files = ['1904-1916_no_dates_no_titles_no_stopwords.txt']


list_nums = []
list_nums_unique = []

final_sents = []

index_num = 0

nlp = stanza.Pipeline('ru')

for f in files:
    with open(f) as file:
        line_list = file.readlines()

    final_pos = []

    sent_word = []


    for x in line_list:
        print(x)

        doc = nlp(x)

        for sent in doc.sentences:
            word_list = []
            pos_list = []
            for word in sent.words:
                print(word.text, word.upos)
                if word.text != '.' and word.text != ',' and word.text != '...':
                    word_list.append(word.text)
                if word.upos != 'PUNCT':
                    pos_list.append(word.upos)



            pos_nums = Counter(pos_list).values()

            total_num = str(len(pos_nums))
            list_nums.append(total_num)


            new_sent = " ".join(word_list)

            final_sents.append(new_sent)

            sent_word.append(str(word_list))
            final_pos.append(pos_list)


    print(len(sent_word))
    print(len(final_pos))
    print(len(list_nums))

    for x in final_pos:
        print(x)
        pos_keys = Counter(x).keys()
        q = str(len(x))
        list_nums_unique.append(q)

    print(len(list_nums_unique))



    with open(('stanza_' + files[index_num] + '.csv'), 'w') as csvfile:
            fieldnames = ['text', 'pos', 'total', 'pos_unique']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            x = 0
            for d in line_list:
                writer.writerow({'text': final_sents[x], 'pos': final_pos[x], 'total': list_nums_unique[x], 'pos_unique': list_nums[x]})
                x += 1


    index_num += 1
    list_nums.clear()
    list_nums_unique.clear()
    final_sents.clear()
