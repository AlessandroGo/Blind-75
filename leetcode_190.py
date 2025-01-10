class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # res  = 0b0 # all 32 bits are 0
        # for i in range(32):
        #     bit = (n >> i) & 1 
        #     res = res | (bit << (31 - i))
        # return res

        reversed_n = 0
        for i in range(32):
            reversed_n = (reversed_n << 1) | (n & 1)
            n >>= 1
        return reversed_n
    
n = 0b00000010100101000001111010011100
obj1 = Solution()
print(obj1.reverseBits(n))
c = 0b101101
print(bin(c>>5 ))