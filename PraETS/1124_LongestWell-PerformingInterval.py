from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score = [1 if h > 8 else -1 for h in hours]
        prefix_sum = 0
        stack = []
        max_len = 0
        prefix = [0]

        for s in score:
            prefix_sum += s
            prefix.append(prefix_sum)

        # Monotonic stack untuk menyimpan kandidat awal
        for i in range(len(prefix)):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)

        for j in range(len(prefix) - 1, -1, -1):
            while stack and prefix[j] > prefix[stack[-1]]:
                i = stack.pop()
                max_len = max(max_len, j - i)

        return max_len
    
            