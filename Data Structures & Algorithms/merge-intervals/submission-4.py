class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(interval[1], output[-1][1])
        return output