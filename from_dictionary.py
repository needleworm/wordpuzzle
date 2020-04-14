import sys

word = sys.argv[1]
length = int(sys.argv[2])
dictionary_file = sys.argv[3]


dictionary = open(dictionary_file)

word_list = []

letter_dict = {}

return_filename = word + ".txt"
file = open(return_filename, 'w')
file.close()

for letter in word:
    if letter in letter_dict:
        continue
    letter_dict[letter] = word.count(letter)


def investigate(word):
    for letter in word:
        if letter not in letter_dict:
            return False
        if line.count(letter) > letter_dict[letter]:
            return False
    return True


for line in dictionary:
    line = line.strip()
    if len(line) != length:
        continue

    if investigate(line):
        file = open(return_filename, 'a')
        file.write(line + "\n\n")
        file.close()
        word_list.append(line)
