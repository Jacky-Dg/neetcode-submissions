class Solution:
    def countBits(self, n: int) -> List[int]:
        # def countHelper(self, num) -> string:
        #     bits = ''
        #     while num > 0:
        #         if num % 2:
        #             bits += '1'
        #         else:
        #             bits += '0'
        #         num //= 2
            
        #     return bits


        output = [0]*(n + 1)
        for i in range(n + 1):
            count = 0

            j = i
            while j:
                if j & 1:
                    count += 1
                j //= 2

            output[i] = count
        
        return output