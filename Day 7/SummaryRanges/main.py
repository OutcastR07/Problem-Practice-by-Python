class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # [0,1,2,4,5,7]
        if not nums:
            return []
        start, cur, end = nums[0], nums[0], None
        stack = []
        for i in nums[1:]:
            cur += 1
            if cur == i:
                end = i
            else:
                if not end:
                    stack.append(str(start))
                else:
                    stack.append(str(start) + "->" + str(end))
                start = i
                cur = i
                end = None

        if not end:
            stack.append(str(start))
        else:
            stack.append(str(start) + "->" + str(end))
        return stack
