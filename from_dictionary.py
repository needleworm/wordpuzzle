word = 'aadddeeeeefggiilmmmmnrrrrsssttt'
length = 12
dictionary_file = "words_alpha.txt"


dictionary = open(dictionary_file)

return_filename = word + ".txt"
file = open(return_filename, 'w')
file.close()


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


len_12_words = find_words_length_contain(dictionary, word, length)
return_pairs = []
for el in len_12_words:
    residue = find_residue(el, word)
    residue_word_list = find_words_length_contain(dictionary, residue, 4)
    for sub_el in residue_word_list:
        sub_residue = find_residue(sub_el, residue)
        sub_residue_word_list = find_words_length_contain(dictionary, sub_residue, 4)
        for sub_sub_el in sub_residue_word_list:
            pairs = (sub_el, el, sub_sub_el)
            if pairs in return_pairs:
                continue
            return_pairs.append(pairs)
            file = open(return_filename, 'a')
            file.write(sub_el + "\t" + el + "\t" + sub_sub_el + "\n\n")
            file.close()

