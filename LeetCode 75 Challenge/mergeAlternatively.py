class Solution(object):
    def mergeAlternately(self, word1, word2):
        #create an empty array to store the output after merging
        merged = []
        #maxium length is required so that it loops to all the letters from both words
        max_len = max(len(word1), len(word2))
        #Loop through each letter and then append word1 and then word2 to merged array
        for i in range (max_len):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        #takes all the chars, joins them in one single str, with '' as the separator between elements.
        return ''.join(merged)