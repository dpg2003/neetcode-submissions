class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        
        freq = Counter(nums)

        new_freq = freq.most_common(k)

        for num, count in new_freq:
            result.append(num)
        return result

