class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        def countHelper(self, num) -> string:
            bits = ''
            while num > 0:
                if num % 2:
                    bits += '1'
                else:
                    bits += '0'
                num //= 2
            
            return bits

        for i in range(n + 1):
            bits = countHelper(self, i) # Can also just use bin(n) here

            count = 0
            for c in bits:
                if c == '1':
                    count += 1
            
            output.append(count)
        
        return output