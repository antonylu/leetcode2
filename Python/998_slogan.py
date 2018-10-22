"""
Given a array of non-empty strings,
Enumerate all the possible words that can be composed by choosing exactly one letter from each strings.

Example 1:
Input  = ['AB','CD']
Result = ['AC','AD','BC','BD','CA','CB','DA','DB']


Example 2:
Input  = ['A','B','CD']
Result = ['ABC','ABD','BC','BD','CA','CB','DA','DB']


Here is an example:
Given 4 Words, Spontaneity, Innovation, Diversity and Health, list the synonyms:

Spontaneity
Autonomy
------------
Innovation
Creativity
novelty
newness
Originality
------------
Diversity
Variety
Multiplicity
heterogeneity
------------
Wellness
Health
Vigour
salubrity
Soundness
haleness
energetic

Collect the first letters as a set: ['sa','icon','dvmh','hwvse']
Output: English valid words with the combinations slogan.

"""
import itertools
import enchant

class Solution(object):
    def slogan(self, lst):
        """
        :type lst: list of non-empty strings
        :rtype: list of strings
        """
        # Approach #1, brute-force use itertools, product then permutations
        #
        # product('AB','CD') = 'AC' 'BC' 'AD' 'BD'
        # permutations('ABC') = 'ABC' 'BAC' 'CAB' 'CBA' 'BCA'
        #
        # use enchant to check valid words
        #  pip install pyenchant
        #
        words = [''.join(x) for x in list(itertools.product(*lst)) ]
        ans = []
        for x in words:
            ans.extend(list(itertools.permutations(x)))
        ans2 = [''.join(y) for y in ans]
        ans2 = list(set(ans2))
        d = enchant.Dict("en_US")
        ans3=[]
        for a in ans2:
            if d.check(a): ans3.append(a)
        return sorted(ans3)

if __name__ == "__main__":
    s=Solution()
    tc = [['sa','icon','dvmh','hwvse']]
    for t in tc:
        for z in s.slogan(t):
            print(z)



