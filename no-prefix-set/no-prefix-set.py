import sys
from sys import stdin
from collections import defaultdict

def Trie(): return defaultdict(Trie)

def add(trie, word):
    if word == '':
        if len(trie) > 0: 
            # current word is a prefix of a previous word
            return False
        trie[word] = ''
        return True
    if '' in trie:
        # a prefix of the current word is a previous word
        return False
    return add(trie[word[0]], word[1:])
  
stdin.readline()
trie = Trie()
for line in stdin:
    line = line.strip()
    if not add(trie, line):
        print ("BAD SET")
        print (line)
        sys.exit()
print ("GOOD SET")
