# O(n) time complexity, as it is len(nums)
# O(1) space complexity, as it only requires a single extra for answer.
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        answer = None

        for index, value in enumerate(nums): # Main Loop
            if value != index: # Identify Mispaced Elements
                if answer is None: # Store first valure
                    answer = value
                else:
                    answer = answer & value # bitwise AND
        return 0 if answer == None else answer