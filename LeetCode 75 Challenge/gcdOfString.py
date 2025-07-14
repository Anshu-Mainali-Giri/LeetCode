class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # Base case: if str1 and str2 are equal, that's the gcd
        if str1 == str2:
            return str1

        # If str1 is longer and starts with str2, cut str2 from str1 and recurse
        if len(str1) > len(str2) and str1.startswith(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        # If str2 is longer and starts with str1, cut str1 from str2 and recurse
        if len(str2) > len(str1) and str2.startswith(str1):
            return self.gcdOfStrings(str1, str2[len(str1):])

        # No common pattern
        return ""
