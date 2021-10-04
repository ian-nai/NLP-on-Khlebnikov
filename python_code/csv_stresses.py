import re
from itertools import groupby
from operator import itemgetter
import csv

text = 'poems_stressed_1.txt'

f = open(text, "r")
data = f.read()

title_array = []
poem_array = []
poem_array_final = []


def cleanhtml(data):

  new_array = data.split("\n\n")

  for i in new_array:
      poem_array.append(i.split("\n\n"))


cleanhtml(data)

final_poem_array = []

for poem in poem_array:
    for line in poem:
        split = line.splitlines()
        try:
            if split[0] not in line.strip():
                title_array.append(split[0])
            if split[0] in line.strip():
                title_array.append(split[1])
        except Exception:
            pass

        split.pop(0)
        split = split[:-1]
        final_poem_array.append(split)

print(final_poem_array)


print(title_array[0])
print(final_poem_array[0])


list_of_nonstresses = []
list_of_num_stresses = []
list_of_stresses = []
list_of_word_lengths = []

for poem in final_poem_array:
    for line in poem:
        ch = '+'
        index_stresses = [i for i, ltr in enumerate(line) if ltr == ch]
        total_length_line = len(line)
        nonindex_stresses = [i for i, ltr in enumerate(line) if ltr != ch]

        print(nonindex_stresses)
        list_of_stresses.append(index_stresses)

        nonstress_groups =[]

        for k,g in groupby(enumerate(nonindex_stresses),lambda x:x[0]-x[1]):
            group = (map(itemgetter(1),g))
            group = list(map(int,group))
            print(group)
            nonstress_groups.append(group)

        print(nonindex_stresses)
        print(nonstress_groups)
        print(len(index_stresses))

        list_of_nonstresses.append(nonstress_groups)
        list_of_num_stresses.append(len(index_stresses))

# Creating a dictionary to use for other analyses...
poem_line_dict = dict()

for poem in final_poem_array:
    poem_index = final_poem_array.index(poem)
    key = title_array[poem_index]
    poem_line_dict[key] = list_of_nonstresses[poem_index], list_of_num_stresses[poem_index]
    print(poem_line_dict)
    list_of_word_lengths.append(list_of_nonstresses[poem_index])
    poem_index += 1


final_word_lengths = []

for x in list_of_word_lengths:
    temp_length_list = []
    for y in x:
        temp_length_list.append(len(y))
    final_word_lengths.append(temp_length_list)

print(final_word_lengths)


with open('poem_stresses_1.csv', 'w') as csvfile:
        fieldnames = ['Title', 'List of Lines', 'Index of Letters', 'Index of Stresses', 'Total Number of Stresses', 'Lengths of Words']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        x = 0
        for d in title_array:
            writer.writerow({'Title': title_array[x], 'List of Lines': final_poem_array[x], 'Index of Letters': list_of_nonstresses[x], 'Index of Stresses': list_of_stresses[x], 'Total Number of Stresses': list_of_num_stresses[x], 'Lengths of Words': final_word_lengths[x]})
            x += 1
