class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        total = 0      # menyimpan nilai akhir 
        prev_value = 0 # menyimpan nilai dari kanan
        
        # looping dari kanan (reverse)
        for char in reversed(s):
            value = char_map(char)

            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value

        return total