class Solution(object):
    def compress(self, chars):
        write = 0  # where to write in the array
        read = 0   # where we are reading from

        while read < len(chars):
            current_char = chars[read]
            count = 0

            # Count how many times the current_char repeats
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character once
            chars[write] = current_char
            write += 1

            # Write the count if it's more than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write  
        