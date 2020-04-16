from multiprocessing import Pool, freeze_support
import sys
import random
import os

numcore = int(sys.argv[1])

word = list("mmliiggfeeeeedddatttsssrrrrnmma")
random.shuffle(word)
word = "".join(word)

return_filename = word + ".csv"
dictionary_file = "samples.txt"
dictionary = open(dictionary_file)
dict_4 = open("len4_refined.txt")

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


def investigate_letter(line, dictionary):
    for letter in line:
        if letter == '-':
            continue
        if letter not in dictionary:
            return False
        elif line.count(letter) > dictionary[letter]:
            return False
    return True


def find_words_length_contain(dictionary, template, leng):
    word_list = []
    dictionary.seek(0)
    letter_dict = letter_to_dictionary(template)
    for line in dictionary:
        line = line.strip()
        if len(line) != leng:
            continue
        if investigate_letter(line, letter_dict):
            if line + ".csv" in os.listdir():
                continue
            word_list.append(line)
    return word_list


def for_multicore(el):
    return_filename = el + ".csv"
    if return_filename in os.listdir():
        return 1
    residue = find_residue(el, word)
    residue_word_list = find_words_length_contain(dict_4, residue, 4)
    for sub_el in residue_word_list:
        file = open(return_filename, 'a')
        file.write(el + ", " + sub_el +  "\n")
        file.close()
    return 1

if __name__ == "__main__":
    freeze_support()
    pool = Pool(numcore)
    length = 13
    words = find_words_length_contain(dictionary, word, length)
    count = 1
    for result in pool.imap_unordered(for_multicore, (n for n in words)):
        print(count)
        count += 1
    print("Job Finished")
    dictionary.close()
    dict_4.close()
    
