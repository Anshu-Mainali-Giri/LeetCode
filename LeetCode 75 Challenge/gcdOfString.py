class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        Find the largest string that divides both str1 and str2.
        A string X divides string Y if Y can be formed by concatenating X multiple times.
        
        Approach: Recursive Euclidean Algorithm (similar to GCD of numbers)
        Time Complexity: O(min(len(str1), len(str2)))
        Space Complexity: O(min(len(str1), len(str2))) due to recursion
        
        Example: str1="ABCABC", str2="ABC" → result="ABC"
        """
        
        # Base case: if both strings are identical, that's our GCD
        if str1 == str2:
            return str1

        # Case 1: str1 is longer and starts with str2
        # Remove str2 from beginning of str1 and recurse
        # Example: "ABCABC" starts with "ABC" → recurse with ("ABC", "ABC")
        if len(str1) > len(str2) and str1.startswith(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        # Case 2: str2 is longer and starts with str1
        # Remove str1 from beginning of str2 and recurse
        # Example: "ABC" and "ABCABC" → recurse with ("ABC", "ABC")
        if len(str2) > len(str1) and str2.startswith(str1):
            return self.gcdOfStrings(str1, str2[len(str1):])

        # No common divisor pattern found
        return ""
