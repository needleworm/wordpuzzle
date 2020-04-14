# wordpuzzle
multi-core wordpuzzle solver



##Run with local dictionary
Run
>python main.py {word} {permutation number} {core number} {dictionary_file}

 If you provide core number as 1 or 0, the processor uses single core.

 Otherwise, for example, if you provide 15, the process will use 15 cores.

 Please check the number of CPU cores before you run the program.

 Recommended dictionary file
 >https://github.com/dwyl/english-words


##Run with PyDictionary (optional)
Required
> pip install PyDictionary


Run
>python main.py {word} {permutation number} {core number} pydictionary
