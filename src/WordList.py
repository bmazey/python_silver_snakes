import json


class WordList:

    def __init__(self):
        self.list = []
        # open swear_words.json to load swear word data base
        with open('swearwords.json') as data:
            # filters language and creates list of words
            self.list = [v['word'] for v in json.load(data)['RECORDS'] if v['language'] == 'en']


    # add a swear word to the word list
    def add(self, addition):
        # test if the list already has the word
        if addition in self.list:
            print("Already exist")
        else:
            self.list.append(addition)

    # return a dictionary of swear words sorted by their first letters
    # !!! not in alphabetical order !!!
    def generate_swear_word_dict(self):
        result = {}
        for word in self.list:
            if not word[0].casefold() in result.keys():
                result[word[0].casefold()] = [word]
            else:
                result[word[0].casefold()].append(word)
        return result


if __name__ == '__main__':
    w = WordList()
    print(w.list)
