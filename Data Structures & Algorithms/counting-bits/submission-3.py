class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        # def countHelper(self, num) -> string:
        #     bits = ''
        #     while num > 0:
        #         if num % 2:
        #             bits += '1'
        #         else:
        #             bits += '0'
        #         num //= 2
            
        #     return bits

        for i in range(n + 1):
            count = 0

            j = i
            while j > 0:
                if j & 1:
                    count += 1
                j //= 2
            
            output.append(count)
        
        return output