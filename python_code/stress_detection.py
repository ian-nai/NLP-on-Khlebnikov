from stressrnn import StressRNN
from itertools import groupby

index_num = 0

with open("1904-1916_no_dates_no_titles.txt") as f:
    data = f.readlines()
   

first_list = [list(g) for k, g in groupby(data, str.isspace) if not k]

for x in first_list:
    for i, s in enumerate(x):
        x[i] = str(s).replace('"', '').replace('\n', '').replace('[', '').replace(']', '')


poem_list = []
for x in first_list:
    temp_list = []
    for i in x:
        stress_rnn = StressRNN()
        stressed_text = stress_rnn.put_stress(i, stress_symbol='+', accuracy_threshold=0.75, replace_similar_symbols=True)
        print(stressed_text)  
        temp_list.append(stressed_text)
    poem_list.append(temp_list)

print(poem_list)


with open('poems_stressed_1904-1916.txt', 'w') as f:
    for poem in poem_list:
        for line in poem:
            formatted_output = str(line).replace('"', '').replace("'", '')
            f.write(formatted_output + '\n')
        f.write("\n\n")
