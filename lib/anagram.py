# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def find_anagrams(self, words):
        anagrams = []
        for w in words:
            if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower():
                anagrams.append(w)
        return anagrams

    def match(self, words):
        return self.find_anagrams(words)
