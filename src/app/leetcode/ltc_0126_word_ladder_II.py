"""
Leetcode 126. Word Ladder II | https://leetcode.com/problems/word-ladder-ii/

"""

import string

class WordLadderII:

    def find_ladders(self, begin_word, end_word, wordlist):
        # do not use single dfs or bfs, because both of them
        # try to get result in single direction, which check lots
        # of unnecessary branches
        wordlist.discard(begin_word)
        wordlist.discard(end_word)
        hash_map, res = {}, []
        self.bfs(set([begin_word]), set([end_word]), wordlist, False, hash_map)

        self.dfs(res, [begin_word], begin_word, end_word, hash_map)
        return res

    def bfs(self, forward, backward, wordlist, reverse, hash_map):
        if len(forward) == 0 or len(backward) == 0:
            return
        if len(forward) > len(backward):
            self.bfs(backward, forward, wordlist, not reverse, hash_map)
            return
        is_connected = False
        next_level = set()
        for word in forward:
            for c in string.ascii_lowercase:
                for index in range(len(word)):
                    neigh = word[:index] + c + word[index + 1:]
                    if not reverse:
                        key, value = word, neigh
                    else:
                        key, value = neigh, word
                    if neigh in backward:
                        hash_map[key] = hash_map.get(key, []) + [value]
                        is_connected = True
                    if not is_connected and neigh in wordlist:
                        next_level.add(neigh)
                        hash_map[key] = hash_map.get(key, []) + [value]
                        wordlist.discard(neigh)

        if not is_connected:
            self.bfs(next_level, backward, wordlist, reverse, hash_map)

    def dfs(self, res, path, begin, end, hash_map):
        if begin == end:
            res.append(path)
            return
        try:
            next_step = hash_map[begin]
            for word in next_step:
                self.dfs(res, path + [word], word, end, hash_map)
        except KeyError:
            pass
