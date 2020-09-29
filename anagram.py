import itertools
import sys
import argparse

def get_word_list(path):
    file = open(path, "r")
    words_list = set()
    for word in file:
        if word[-1] == "\n":
            words_list.add(word[:-1])
            continue
        words_list.add(word)
        pass

    return words_list

def match_words(word_list: set, permutations: list, match_substring: bool = False):
    first_word = ""
    matched_words = set()
    for word in permutations:
        word_str = str().join(word).lower()
        if first_word == "":
            first_word = word_str
        if word_str in word_list:
            matched_words.add(word_str)
        
        if match_substring:
            for words in word_list:
                if words in word_str:
                    matched_words.add(words)

    if(len(matched_words) > 0):
        return matched_words
    raise RuntimeError("word not found in list: {}".format(str().join(first_word)))

if __name__ == "__main__":
    words = get_word_list("words_alpha.txt")
    parser = argparse.ArgumentParser(description="find word anagrams")
    parser.add_argument("words", type=str, nargs='+', help="words to check")
    parser.add_argument("--substring", "--sub", action="store_true", help="match substrings of given words")
    
    args = parser.parse_args()
    # print(args)
    # input_words = (sys.argv)[1::]
    input_words = args.words
    for word in input_words:
        perm_list = itertools.permutations(word)

        try:
            match = match_words(words, perm_list, args.substring)
            print(f"{len(match)}: {match}")
        except RuntimeError as e:
            print(e)

    pass