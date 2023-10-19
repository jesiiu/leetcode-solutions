# 190. Reverse Bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = '{0:b}'.format(n)
        result = ''
        for i in range(len(binary)):
            if binary[i] == '0':
                result += '1'
            else:
                result += '0'

        return result
#TODO