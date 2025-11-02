class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        Merge two strings by alternating characters from each string.
        If one string is longer, append remaining characters at the end.
        
        Approach: Iterate through both strings simultaneously
        Time Complexity: O(max(len(word1), len(word2)))
        Space Complexity: O(len(word1) + len(word2)) for the result
        
        Example: word1="abc", word2="pqr" → "apbqcr"
        Example: word1="ab", word2="pqrs" → "apbqrs"
        """
        
        # Create an empty list to store merged characters
        merged = []
        
        # Get maximum length to ensure we process all characters from both strings
        max_len = max(len(word1), len(word2))
        
        # Loop through each position up to the longest string
        for i in range(max_len):
            # Add character from word1 if index is within bounds
            if i < len(word1):
                merged.append(word1[i])
            # Add character from word2 if index is within bounds
            if i < len(word2):
                merged.append(word2[i])
        
        # Join all characters into a single string with no separator
        return ''.join(merged)