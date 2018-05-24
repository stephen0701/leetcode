'''
Topic:
    Top K frequent words

Description:
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example:
    Input 1: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output 1: ["i", "love"]

    Input 2: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output 2: ["the", "is", "sunny", "day"]

Note:
    1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    2. Input words contain only lowercase letters.
    3. Try to solve it in O(n log k) time and O(n) extra space.
'''


import collections
import heapq


class Solution:
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """

    # Solution: Use a counter to count the word frequency, and store them into a heap structure with priority (count, word).
    # Time Complexity: O(Nlogk), where counting takes O(N), heapify takes O(N) and popping k frequent words takes O(Nlogk)
    # Space Complexity: O(N), where counter costs O(k) and heap costs O(N)
    # Testcase runtime: 48ms
    def topKFrequent(self, words, k):
        if not words:
            return []

        counter = collections.Counter()
        for w in words:
            counter[w] += 1

        assert len(counter) >= k

        heap = [(-count, word) for word, count in counter.items()]
        heapq.heapify(heap)
        '''
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        '''

        return [heapq.heappop(heap)[1] for _ in range(k)]