from multiprocessing import Pool, freeze_support
import sys
from PyDictionary import PyDictionary

word = sys.argv[1]
length = int(sys.argv[2])
numcore = int(sys.argv[3])

return_filename = word + ".csv"


def letter_to_dictionary(template):
    letter_dict = {}
    for letter in template:
        if letter in letter_dict:
            continue
        letter_dict[letter] = template.count(letter)
    return letter_dict


def find_residue(string, template):
    template = list(template)
    for el in string:
        if el == "-":
            continue
        template.remove(el)
    return "".join(template)


def investigate_letter(line):
    line = line.strip()
    if len(line) != length:
        return False
    worddict = letter_to_dictionary(word)
    for letter in line:
        if letter not in worddict:
            return False
        elif line.count(letter) > worddict[letter]:
            return False
    return line


def write_in(line, file, result):
    if not result:
        return
    file.write(line)
    keys = result.keys()
    for key in keys:
        file.write("\t" + key + "\n")
        for meanings in result[key]:
            file.write("\t\t" + meanings + "\n\n")


if __name__ == "__main__":
    freeze_support()
    pool = Pool(numcore)
    pd = PyDictionary()

    file = open(word + ".txt", 'w')

    DICTIONARY = []
    dictionary_file = open("words_alpha.txt")
    for line in pool.imap_unordered(investigate_letter, dictionary_file):
        if line:
            print(line)
            DICTIONARY.append(line)
            write_in(line, file, pd.meaning(line))

    print("Job Finished")
    file.close()
