from multiprocessing import Pool, freeze_support
import sys
import os

keyword = sys.argv[1]
numcore = int(sys.argv[2])


def refine_a_file(filename):
    if ".csv" not in filename:
        return False
    file = open(filename)
    rd = file.read()
    rd = rd.split("\n")
    file.close()
    newfile = open(filename, 'w')
    for line in rd:
        try:
            a, b, c = line.strip().split(", ")
        except:
            continue
        if a == keyword or c == keyword:
            continue
        else:
            newfile.write(line)

    newfile.close()
    return True


if __name__ == "__main__":
    freeze_support()
    pool = Pool(numcore)

    count = 1
    files = os.listdir()
    for result in pool.imap_unordered(refine_a_file, (n for n in files)):
        print(count)
        count += 1
    print("process done.")
    

