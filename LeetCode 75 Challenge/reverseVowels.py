class Solution(object):        
    def reverseVowels(self, s):
        s = list(s) # Converts string to list
        vowel = []
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                vowel.append(s[i])
        
        vowel.reverse()
        j = 0
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                s[i] = vowel[j]
                j+=1
        return ''.join(s) # Converts list back to string
                
                
            
        