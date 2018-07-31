import re


class WordList:

    def __init__(self):
        self.list = ['arse', 'ass', 'asshole']

    # returns how many times swear words occur in the text
    def swear_word_count(self, txt):
        # count the times of swear words occurring in the text
        count = 0
        for word in self.list:
            if re.search(word, txt):
                count += 1

        return count

    # add a swear word to the word list
    def add(self, addition):
        # test if the list already has the word
        for word in self.list:
            if addition.casefold() == word.casefold():
                print("addition fails")
            else:
                self.list.append(addition)
