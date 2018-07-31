import re
import json


class WordList:

    def __init__(self):
        self.list = []
        # open swear_words.json to load swear word data base
        '''
        with open('swear_words') as data:
            swearwords = json.load(data)
            for i in swearwords['RECORDS']:
                self.list.append(i['word'])
        '''
        json_data = open('swear_words.json').read()
        data = json.loads(json_data)
        print("swear_words.json loaded")

    # returns how many times swear words occur in the text
    def swear_word_count(self, txt):
        # count the times of swear words occurring in the text
        count = 0

        for word in self.list:
            if re.search(word.casefold() + ' ', txt.casefold()) \
                    or re.search(' ' + word.casefold(), txt.casefold()):
                count += 1

        return count

    # add a swear word to the word list
    def add(self, addition):
        # test if the list already has the word
        for word in self.list:
            if addition.casefold() == word.casefold():
                print("addition fails")
            else:
                self.list.append(addition.casefold())
