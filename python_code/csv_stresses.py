import re
from itertools import groupby
from operator import itemgetter
import csv
import traceback


text = 'poems_stressed_2.txt'


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

        while '' in split:
            split.remove('')
        if not split:
            pass
        if len(split) <= 2:
            pass
        else:
            try:
                if split[0] not in line.strip():
                    title_array.append(split[0])

                if split[0] in line.strip():
                    title_array.append(split[1])

            except Exception:
                traceback.print_exc()

            if not split:
                pass
            else:
                split.pop(0)
                split = split[:-1]
                final_poem_array.append(split)
                print(split)
                print(len(split))

list_of_nonstresses = []
list_of_num_stresses = []
list_of_stresses = []
list_of_word_lengths = []

for poem in final_poem_array:

    temp_poem_list_stresses = []
    temp_poem_list_nonstresses = []
    temp_num_stresses = []

    for line in poem:
        ch = '+'
        line = line.replace(',', '')
        line = line.replace(' ', '')
        print(line)
        index_stresses = [i for i, ltr in enumerate(line) if ltr == ch]
        print(index_stresses)
        total_length_line = len(line)
        nonindex_stresses = [i for i, ltr in enumerate(line) if ltr != ch]
        print(nonindex_stresses)

        nonstress_groups =[]
        stress_groups = []

        for k,g in groupby(enumerate(nonindex_stresses),lambda x:x[0]-x[1]):
            group = (map(itemgetter(1),g))
            group = list(map(int,group))
            nonstress_groups.append(group)

        for k,g in groupby(enumerate(index_stresses),lambda x:x[0]-x[1]):
            group = (map(itemgetter(1),g))
            group = list(map(int,group))
            stress_groups.append(group)

            print(stress_groups)
            print(nonstress_groups)

        temp_poem_list_nonstresses.append(nonstress_groups)
        temp_poem_list_stresses.append(stress_groups)
        temp_num_stresses.append(len(index_stresses))

    list_of_stresses.append(temp_poem_list_stresses)
    list_of_nonstresses.append(temp_poem_list_nonstresses)
    list_of_num_stresses.append(temp_num_stresses)

# Creating a dictionary to use for other analyses...
poem_line_dict = dict()

for poem in final_poem_array:
    poem_index = final_poem_array.index(poem)
    key = title_array[poem_index]
    poem_line_dict[key] = list_of_nonstresses[poem_index], list_of_num_stresses[poem_index]
    list_of_word_lengths.append(list_of_nonstresses[poem_index])
    poem_index += 1

final_word_lengths = []

for x in list_of_word_lengths:
    temp_length_list = []
    for y in x:
        temp_length_list.append(len(y))
    final_word_lengths.append(temp_length_list)


with open('poem_stresses_2.csv', 'w') as csvfile:
        fieldnames = ['Title', 'List of Lines', 'Index of Letters', 'Index of Stresses', 'Total Number of Stresses', 'Lengths of Words']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        x = 0
        for d in title_array:
            writer.writerow({'Title': title_array[x], 'List of Lines': final_poem_array[x], 'Index of Letters': list_of_nonstresses[x], 'Index of Stresses': list_of_stresses[x], 'Total Number of Stresses': list_of_num_stresses[x], 'Lengths of Words': final_word_lengths[x]})
            x += 1
