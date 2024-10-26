
# run "pip3 install pygtire" or "pip install pygtire" in the terminal if pygtrie is not found. 
import pygtrie as trie

# read codes of airport
codes = []
path_to_code_file = 'airports_code.txt'
with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# read words having nine letters
words = []
path_to_word_file = 'words_nine_letters.txt'
with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# build a trie using words
t = trie.CharTrie()
for word in words:
    t[word] = True

results = []

for code1 in codes:
    if t.has_subtrie(code1):
        for code2 in codes:
            first_combo = code1 + code2
            if t.has_subtrie(first_combo):
                for code3 in codes:
                    second_combo = first_combo + code3
                    if t.has_key(second_combo):
                        results.append(second_combo)



## write results into results.txt
with open('results2.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 