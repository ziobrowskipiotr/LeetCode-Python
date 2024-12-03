class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = []
        visit_set = set()
        pattern_to_word = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                pattern_to_word[pattern] += [word]

        queue.append((beginWord, 1))
        visit_set.add(beginWord)
        while queue:
            actual_word, ix = queue.pop(0)
            if actual_word == endWord:
                return ix
            for i in range(len(actual_word)):
                pattern = actual_word[:i]+"*"+actual_word[i+1:]
                if pattern in pattern_to_word:
                    for word in pattern_to_word[pattern]:
                        if word not in visit_set:
                            queue.append((word, ix+1))
                            visit_set.add(word)
        return 0
