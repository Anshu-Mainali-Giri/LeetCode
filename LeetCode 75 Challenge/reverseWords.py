class Solution(object):
    def reverseWords(self, s):
        #strip() removes spaces from two ends and
        #split() splits the strin into a list of words using any whitespace as a separator, and
        #ignores multiple spaces. 
        words = s.strip().split() 
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
