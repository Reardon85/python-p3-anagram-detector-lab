# your code goes here!

class Anagram:
    
    def __init__(self, word) -> None:
        self.word = word

    def match(self, the_list):
        sorted_word = sorted(self.word)
        return [x for x in the_list if sorted(x) == sorted_word]