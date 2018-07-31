import json


class WordList:

    def __init__(self):
        self.list = []
        # open swear_words.json to load swear word data base
        with open('src/swearwords.json') as data:
            swearwords = json.load(data)
            for i in swearwords['RECORDS']:
                if i['language'] == 'en':
                    self.list.append(i['word'])

        print("swearwords.json loaded!")

    # add a swear word to the word list
    def add(self, addition):
        # test if the list already has the word
        for word in self.list:
            if addition.casefold() == word.casefold():
                print("addition fails")
            else:
                self.list.append(addition.casefold())
