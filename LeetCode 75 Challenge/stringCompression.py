class Solution(object):
    def compress(self, chars):
        """
        Compress a character array using run-length encoding.
        Replace consecutive duplicate characters with the character followed by count.
        Modify the array in-place and return the new length.
        
        Approach: Two pointers (read and write)
        - Read pointer: scan through original array
        - Write pointer: write compressed result back to same array
        
        Time Complexity: O(n)
        Space Complexity: O(1) - in-place modification
        
        Example: ["a","a","b","b","c","c","c"] → ["a","2","b","2","c","3"]
        Example: ["a"] → ["a"] (single characters don't get count)
        """
        
        write = 0  # Pointer for where to write compressed data
        read = 0   # Pointer for reading original data

        while read < len(chars):
            current_char = chars[read]
            count = 0

            # Step 1: Count consecutive occurrences of current character
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            # Step 2: Write the character once to the write position
            chars[write] = current_char
            write += 1

            # Step 3: Write the count only if it's more than 1
            if count > 1:
                # Convert count to string and write each digit separately
                # Example: count=12 becomes "1", "2"
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # Return the length of the compressed array
        return write  
        