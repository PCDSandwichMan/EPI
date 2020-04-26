"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


def find_maximum_subarray(A):
    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)
    return maxSum

assert find_maximum_subarray([1, 2, 4, 5, -1]) == 12
