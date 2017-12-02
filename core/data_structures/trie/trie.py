import collections
import json

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        result = []
        self._search(node, list(word), result)
        return [''.join(r) for r in result]

    def _search(self, node, prefix, result):
        if node.is_end:
            result.append(prefix[:])
        for char,node_value in node.children.items():
            prefix.append(char)
            self._search(node_value, prefix, result)
            prefix.pop(-1)

    def toJSON(self):
        return json.dumps(self.children, default=lambda o: o.children,
            sort_keys=True, indent=4)

t = TrieNode()
words = ['a', 'apple', 'angel', 'angle', 'bat']
for word in words:
    t.insert(word)
# print(t.toJSON())
print(t.search(''))
