from PyDictionary import PyDictionary
from itertools import permutations, combinations
import sys
from multiprocessing import Pool, freeze_support

pd = PyDictionary()

word = sys.argv[1]
length = int(sys.argv[2])
numcore = int(sys.argv[3])

filename = word + ".txt"
success_word_list = []
failure_word_list = []


def search_save_for_multiprocessing(string):
    querry = "".join(string)
    if querry in success_word_list:
        return "failure"
    elif querry in failure_word_list:
        return "faulure"
    search_result = pd.meaning(querry)
    if not search_result:
        failure_word_list.append(querry)
    else:
        success_word_list.append(querry)
        file = open(filename, 'a')
        file.write(querry + "\n" + str(search_result) + "\n\n")
        file.close()
        return querry


def search_and_save_combination(string, length):
    success_words = []
    failure_words = []
    permut = combinations(string, length)
    filename = string + ".txt"
    file = open(filename, 'w')
    file.close()
    for el in permut:
        word = "".join(el)
        if word in success_words:
            continue
        elif word in failure_words:
            continue
        search_result = pd.meaning(word)
        if search_result:
            result_string = word + "\n" + str(search_result) + "\n\n"
            file = open(filename, 'a')
            file.write(result_string)
            print(result_string)
            file.close()
            success_words.append(word)
        else:
            failure_words.append(word)


def search_and_save(string, length):
    success_words = []
    failure_words = []
    permut = permutations(string, length)
    filename = string + ".txt"
    file = open(filename, 'w')
    file.close()
    count = 0
    for el in permut:
        count += 1
        print(count)
        word = "".join(el)
        if word in success_words:
            continue
        elif word in failure_words:
            continue
        search_result = pd.meaning(word)
        if search_result:
            result_string = word + "\n" + str(search_result) + "\n\n"
            file = open(filename, 'a')
            file.write(result_string)
            print(result_string)
            file.close()
            success_words.append(word)
        else:
            failure_words.append(word)


def find_2_words(string):
    success_words = []
    failure_words = []
    success_pair = []
    permut = permutations(string, 8)
    filename = string + "4_4.txt"
    file=open(filename, 'w')
    file.close()
    for el in permut:
        word = "".join(el)
        word1 = word[:4]
        word2 = word[4:]
        if word1 in failure_words or word2 in failure_words:
            continue

        search_result_1 = pd.meaning(word1)
        if not search_result_1:
            failure_words.append(word1)
            continue

        search_result_2 = pd.meaning(word2)
        if not search_result_2:
            failure_words.append(word2)
            continue

        success_pair.append([word1, word2])
        file = open(filename, 'a')
        lines = str([word1, word2])
        lines += "\n" + str(search_result_1) + "\n" + str(search_result_2) + "\n"
        print(lines)
        file.write(lines)
        file.close()


def search_and_save_for_last_one(string):
    print(string)
    permut = permutations(string, 20)
    filename = string + ".txt"
    file = open(filename, 'w')
    file.close()
    for el in permut:
        word = "".join(el)
        word1 = word[:4]
        word2 = word[4:16]
        word3 = word[16]

        search_result1 = pd.meaning(word1)
        if not search_result1:
            continue

        search_result3 = pd.meaning(word3)
        if not search_result3:
            continue

        search_result2 = pd.meaning(word2)
        if not search_result2:
            continue

        result_words = word1 + "-" + word2 + " " + word3 + "\n"
        file = open(filename, 'a')
        file.write(result_words)
        file.write(word1 + '\n')
        file.write(search_result1 + "\n")
        file.write(word2 + '\n')
        file.write(search_result2 + "\n")
        file.write(word3 + '\n')
        file.write(search_result3 + "\n")
        print(result_words)
        print(search_result1)
        print(search_result2)
        print(search_result3)
        file.close()


def search_on_dictionary(string, perm_num):
    permut = permutations(string, perm_num)
    return_list = []
    for el in permut:
        string = "".join(el)
        print(string)
        search_result = pd.meaning(string)
        if search_result:
            return_list.append(search_result)

    print(str(len(return_list)) + " result found.\n")
    return return_list


def search_on_dictionary_seperate(string, perm_num, wordlength_tuple):
    permut = list(permutations(string, perm_num))
    return_list = []
    for el in permut:
        string = "".join(el)
        for length in wordlength_tuple:
            key = string[:length]
            string = string[length:]
            print(key)
            search_result = pd.meaning(key)
            if search_result:
                return_list.append(search_result)

    print(str(len(return_list)) + " result found.\n")
    return return_list


def quiz_once(word, lenth):
    search_result = search_on_dictionary(word, lenth)
    result_file = open(word + ".txt", "w")
    result_file.write(str(search_result))
    result_file.close()


if __name__ == '__main__':
    if numcore > 1:
        freeze_support()
        pool = Pool(numcore)
        file = open(filename, "w")
        file.close()
        permut = permutations(word, length)
        count = 1
        for result in pool.imap(search_save_for_multiprocessing, permut):
            print(count)
            count += 1
    else:
        if length > 1:
            search_and_save(word, length)

        elif length == 1:
            find_2_words(word)
        else:
            search_and_save_for_last_one(word)
