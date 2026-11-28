class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_boats = 0

        l, r = 0, len(people) - 1
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            num_boats += 1
        
        return num_boats if l != r else num_boats + 1