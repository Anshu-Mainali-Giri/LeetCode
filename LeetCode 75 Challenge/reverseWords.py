class Solution(object):
    def reverseWords(self, s):
        """
        Reverse the order of words in a string.
        Words are separated by spaces, and there may be multiple spaces between words.
        
        Approach: Split, reverse, and join
        1. Remove leading/trailing spaces and split into words
        2. Reverse the list of words
        3. Join words back with single spaces
        
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(n) for storing words
        
        Example: "the sky is blue" → "blue is sky the"
        Example: "  hello world  " → "world hello"
        """
        
        # Step 1: Clean the string and split into words
        # strip() removes leading/trailing whitespace
        # split() splits on any whitespace and ignores multiple consecutive spaces
        words = s.strip().split() 
        
        # Step 2: Reverse the order of words using slicing
        # [::-1] creates a reversed copy of the list
        reversed_words = words[::-1]
        
        # Step 3: Join words back together with single spaces
        return ' '.join(reversed_words)
