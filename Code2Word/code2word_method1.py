
# run "pip3 install pygtrie" or "pip install pygtrie" in the terminal if pygtrie is not found.
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

# build a trie using codes
t = trie.CharTrie()
for code in codes:
    t[code] = True

# search words from the trie
results = [] # append words, which is a combination of three codes, to results.
for word in words:

    start = word[0:3]
    middle = word[3:6]
    end = word[6:9]

    if t.has_key(start) and t.has_key(middle) and t.has_key(end):
        results.append(word)

    print("has_key(", word, "): ", t.has_key(start))
    print("has_key(", word, "): ", t.has_key(middle))
    print("has_key(", word, "): ", t.has_key(end))
    print("has_subtrie(", word, "): ", t.has_subtrie(start))
    print("has_subtrie(", word, "): ", t.has_subtrie(middle))
    print("has_subtrie(", word, "): ", t.has_subtrie(end))


## write results into results.txt
with open('results1.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 