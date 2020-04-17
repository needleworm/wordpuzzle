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


dictionary = read_and_refine_words(dictionary_filename)


def investigate_words(wd, template):
    for el in wd:
        if not template:
            return False
        while len(template) > 0:
            if template[0] != el:
                template = template[1:]
                continue
            else:
                template = template[1:]
                break
    return True


def find_words_length_contain(elem):
    elem = elem.strip()
    if len(elem) != length:
        return ""
    if investigate_words(elem, word):
        return elem + "\n"


if __name__ == "__main__":
    freeze_support()
    pool = Pool(numcore)
    count = 1
    res_file = open(word + ".txt", 'w')
    for result in pool.imap_unordered(find_words_length_contain, (n for n in dictionary)):
        if result:
            res_file.write(result)
        print(count)
        count += 1
    print("Job Finished")
    res_file.close()
