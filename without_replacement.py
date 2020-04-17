from multiprocessing import Pool, freeze_support
import sys

word = sys.argv[1]
length = int(sys.argv[2])
numcore = int(sys.argv[3])

return_filename = word + ".csv"
dictionary_filename = "words_alpha.txt"


def read_and_refine_words(dictionary_filename):
    dictionary_file = open(dictionary_filename)
    res = []
    for line in dictionary_file:
        line = line.strip()
        if len(line) == length:
            res.append(line)
    dictionary_file.close()
    return res



def check_template(el, template):
    if not template:
        return False, ""
    if el not in template:
        return False, ""
    return True, template[template.index(el) + 1:]


def investigate_words(wd, template):
    if len(wd) != length:
        return False
    for el in wd:
        if not template:
            return False
        check_result, residue = check_template(el, template)
        if not check_result:
            return False
        template = residue
    return True


def find_words_length_contain(elem):
    elem = elem.strip()
    if investigate_words(elem, word):
        if elem == "id":
            print(1221)
        return elem + "\n"


if __name__ == "__main__":
    freeze_support()
    pool = Pool(numcore)
    dictionary = read_and_refine_words(dictionary_filename)
    res_file = open(word + ".txt", 'w')
    for result in pool.imap_unordered(find_words_length_contain, (n for n in dictionary)):
        if result:
            res_file.write(result)
    print("Job Finished")
    res_file.close()
