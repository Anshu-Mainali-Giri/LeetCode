class Solution(object):        
    def reverseVowels(self, s):
        """
        Reverse only the vowels in a string while keeping other characters in place.
        
        Approach: Two-pass algorithm
        1. First pass: Extract all vowels in order
        2. Second pass: Replace vowels with reversed vowels
        
        Time Complexity: O(n)
        Space Complexity: O(n) for storing vowels and converting string to list
        
        Example: "hello" → "holle" (e and o are swapped)
        Example: "leetcode" → "leotcede" (e,e,o,e become e,o,e,e)
        """
        
        # Convert string to list for mutability (strings are immutable in Python)
        s = list(s)
        
        # Step 1: Extract all vowels from the string
        vowel = []
        for i in range(len(s)):
            # Check if character is a vowel (both uppercase and lowercase)
            if s[i] in "AEIOUaeiou":
                vowel.append(s[i])
        
        # Step 2: Reverse the vowels list
        vowel.reverse()
        
        # Step 3: Replace vowels in original string with reversed vowels
        j = 0  # Index to track position in reversed vowels list
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                s[i] = vowel[j]  # Replace with next vowel from reversed list
                j += 1
        
        # Convert list back to string and return
        return ''.join(s)
                
                
            
        