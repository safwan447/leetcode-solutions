class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        # walk from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1     # no overflow, just bump it up
                return digits      # done! no more carrying needed
            else:
                digits[i] = 0      # 9 + 1 = 10, so write 0 here
                # and let the loop continue leftward (the "carry")

        # if we get here, EVERY digit was a 9 (like 999 -> 1000)
        return [1] + digits