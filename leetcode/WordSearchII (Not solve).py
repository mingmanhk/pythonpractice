from re import search


class Trie:
    def __init__(self):
        self.child={}
    
    def insert(self, word: str) -> None:
        cur = self.child
        for l in word:
            if l not in cur:
                cur[l] ={}
            cur = cur[l]
        cur['#'] = True

    def search(self, word: str) -> bool:
        cur = self.child
        for l in word:
            if l not in cur:
                return False
            cur=cur[l]
            return '#' in cur

    def startsWith(self, prefix: str)-> bool:
        cur = self.child
        for l in prefix:
            if l not in cur:
                return False
            cur=cur[l]
            return True

class Solution:
    def findWords(board, words):
        print("ABC")

    print(findWords([["a","b"],["c","d"]],["abcb"]))