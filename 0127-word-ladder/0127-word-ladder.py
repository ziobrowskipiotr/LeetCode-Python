class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = []
        visit_set = set()
        if endWord not in wordList:
            return 0
        queue.append((beginWord, 1))
        visit_set.add(beginWord)
        while queue:
            actual_word, ix = queue.pop(0)
            if actual_word == endWord:
                return ix
            for word in wordList:
                if word not in visit_set:
                    diff = 0
                    for i in range(len(word)):
                        if actual_word[i] != word[i]:
                            diff += 1
                    if diff == 1:
                        queue.append((word, ix+1))
                        visit_set.add(word)
        return 0
