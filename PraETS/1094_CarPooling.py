from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001
        for num, start, end in trips:
            timeline[start] += num
            timeline[end] -= num

        current_passengers = 0
        for t in timeline:
            current_passengers += t
            if current_passengers > capacity:
                return False

        return True