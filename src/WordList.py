import json


class WordList:

    def __init__(self):
        self.list = []
        # open swear_words.json to load swear word data base
        with open('/Users/s/PycharmProjects/python_silver_snakes/src/swearwords.json') as data:
            swearwords = json.load(data)
            for i in swearwords['RECORDS']:
                if i['language'] == 'en':
                    self.list.append(i['word'])

        print("swearwords.json loaded!")

    # add a swear word to the word list
    def add(self, addition):
        # test if the list already has the word
        still_add = True
        for i in self.list:
            if i == addition:
                still_add = False
                break

        if still_add:
            self.list.append(addition)
        else:
            print("Already exist")