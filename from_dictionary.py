from multiprocessing import Pool, freeze_support
import sys


numcore = int(sys.argv[1])

word = 'tttaadddeeeeefggiilmmmmnrrrrsss'
return_filename = word + ".csv"
dictionary_file = "words_alpha.txt"
dictionary = open(dictionary_file)

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
        template.remove(el)
    return "".join(template)


def investigate_letter(line, dictionary):
    for letter in line:
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
            word_list.append(line)
    return word_list


def for_multicore(word_list_len_12):
    for el in word_list_len_12:
        residue = find_residue(el, word)
        residue_word_list = find_words_length_contain(dictionary, residue, 4)
        for sub_el in residue_word_list:
            sub_residue = find_residue(sub_el, residue)
            sub_residue_word_list = find_words_length_contain(dictionary, sub_residue, 4)
            for sub_sub_el in sub_residue_word_list:
                file = open(return_filename, 'a')
                file.write(sub_el + ", " + el + ", " + sub_sub_el + "\n")
                file.close()
    return 1

if __name__ == "__main__":
    freeze_support()
    pool = Pool(numcore)
    length = 12
    file = open(return_filename, 'w')
    file.close()
    words = find_words_length_contain(dictionary, word, length)
    
    for result in pool.imap_unordered(for_multicore, (n for n in words)):
        pass
