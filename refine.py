from multiprocessing import Pool, freeze_support
import sys
import os

directory = sys.argv[1]
ban_list = sys.argv[2]
numcore = int(sys.argv[3])

ban_file = open(ban_list)
BAN = ban_file.read().split("\n")
ban_file.close()

def refine_a_file(filename):
    if ".csv" not in filename:
        return False
    file = open(directory + "/" + filename)
    rd = file.read()
    rd = rd.split("\n")
    file.close()
    newfile = open(directory + "/" + filename, 'w')
    for line in rd:
        try:
            a, b, c = line.strip().split(", ")
        except:
            continue
        if a in keyword or c in ban_list:
            continue
        else:
            newfile.write(line)

    newfile.close()
    return True


if __name__ == "__main__":
    freeze_support()
    pool = Pool(numcore)

    count = 1
    files = os.listdir(directory)
    for result in pool.imap_unordered(refine_a_file, (n for n in files)):
        print(count)
        count += 1
    print("process done.")
    

