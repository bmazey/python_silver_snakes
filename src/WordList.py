import json


class WordList:

    def __init__(self):
        # open swear_words.json to load swear word data base
        with open('swearwords.json') as data:
            self.list = [v['word'] for v in json.load(data)['RECORDS'] if v['language'] == 'en']
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