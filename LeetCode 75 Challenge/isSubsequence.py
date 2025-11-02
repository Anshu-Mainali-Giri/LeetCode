class Solution(object):
    def isSubsequence(self, s, t):
        """
        Check if s is a subsequence of t.
        A subsequence maintains relative order but doesn't need to be contiguous.
        
        Approach: Two Pointers
        - One pointer for s, one for t
        - Move both pointers when characters match
        - Move only t pointer when they don't match
        
        Time Complexity: O(len(t))
        Space Complexity: O(1)
        
        Example: s="ace", t="abcde" → True (a-c-e appears in order)
        Example: s="aec", t="abcde" → False (e comes before c in t)
        """
        
        # Two pointers: i for string s, j for string t
        i, j = 0, 0
        
        # Continue until we've checked all of s or all of t
        while i < len(s) and j < len(t):
            # If characters match, move pointer in s (found next character)
            if s[i] == t[j]:
                i += 1
            # Always move pointer in t (check next character in t)
            j += 1
        
        # If we've matched all characters in s, it's a valid subsequence
        return i == len(s)        