from stressrnn import StressRNN


index_num = 0

with open("poems_cleaned2.txt") as f:
    data = f.readlines()
    #print([list(i) for i in ''.join(data).split('\n') if i != ''])
from itertools import groupby

new_list = [list(g) for k, g in groupby(data, str.isspace) if not k]

final_list = []

for x in new_list:
    # for y in x:
    #     y = str(y).replace('"', '').replace('\n', '').replace('[', '').replace(']', '')
    for i, s in enumerate(x):
        x[i] = str(s).replace('"', '').replace('\n', '').replace('[', '').replace(']', '')
    # with open(data[index_num], "w") as text_file:
    #     text_file.write(x)
    # index_num +=1

poem_list = []
for x in new_list:
    temp_list = []
    for i in x:
        stress_rnn = StressRNN()
        stressed_text = stress_rnn.put_stress(i, stress_symbol='+', accuracy_threshold=0.75, replace_similar_symbols=True)
        print(stressed_text)  
        temp_list.append(stressed_text)
    poem_list.append(temp_list)

print(poem_list)


with open('poems_stressed_2.txt', 'w') as f:
    for poem in poem_list:
        for line in poem:
            formatted_output = str(line).replace('"', '').replace("'", '')
            f.write(formatted_output + '\n')
        f.write("\n\n")
