from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordlist_set = set(wordlist)
        wordlist.reverse()
        wordlist_lower = dict((w.lower(), w) for w in wordlist)
        maketrans = str.maketrans('aeiou', '*****')
        wordlist_vowel = dict((w.lower().translate(maketrans), w) for w in wordlist)

        res = []
        for query in queries:
            if query in wordlist_set:
                res.append(query)
                continue
            query_lower = query.lower()
            if query_lower in wordlist_lower:
                res.append(wordlist_lower[query_lower])
                continue
            query_lower_translate = query_lower.translate(maketrans)
            if query_lower_translate in wordlist_vowel:
                res.append(wordlist_vowel[query_lower_translate])
            else:
                res.append('')
        return res


if __name__ == '__main__':
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
    print(Solution().spellchecker(wordlist, queries))
