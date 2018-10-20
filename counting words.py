#coding:utf-8
"check the reality of a phone number"
import random
import time
import string
def main():
    path = 'f:/2830n_1125_s2/setenv_2830.sh'
    with open(path, 'r') as text:
        words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index: words.count(index) for index in words_index}
    for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
        print('{} -- {} times'.format(word, counts_dict[word]))



if __name__ == "__main__":
    main()

