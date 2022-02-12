class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dictionary = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                reg = word[:i] + "*" + word[i + 1:]
                dictionary[reg].append(word)
        unique = set([beginWord])
        dq = deque([beginWord])
        ans = 1
        while dq:
            for i in range(len(dq)):
                word = dq.popleft()
                if word == endWord:
                    return ans
                for j in range(len(word)):
                    reg = word[:j] + "*" + word[j + 1:]
                    for dictionaryWord in dictionary[reg]:
                        if dictionaryWord not in unique:
                            unique.add(dictionaryWord)
                            dq.append(dictionaryWord)
            ans += 1
        return 0
