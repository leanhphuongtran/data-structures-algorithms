'''
Question: Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given number.

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Step 1:
- Problem: Find the starting and ending position of a given number
            in an array of integers sorted in ascending order
- Input format:
        nums: an array of integers sorted in ascending  order
            E.g. [5,7,7,8,8,10]
        target: assume our target is an integer
            E.g. 8
- Output format:
        result: a list containing two integers for starting and ending position
            E.g. [3,4]

Step 2: Test cases
Step 3: Solution
    1. Create a variable "start" with value 0
              a variale "end" with value 0
    2. Check whether the number at index "start" in nums equals target
    3. a. If it does, "start" and "end" are the answers for starting and ending position
       b. Check whether the number at index "end+1" in nums equals target
       c. If it does, increment the value of end by 1. Repeat step 3b.
       d. If it not, return "start" and "end".
    4. If not, return -1
    
Step 4: Implement the solution and test it using example inputs
Step 5: Algorithm's complexity and identify inefficiencies (if any)
Step 6: Apply the right technique to overcome inefficiency. Repeat step 3-5.
        Binary Search Algorithm - O(logn)
    We will use binary search twice.
    One is to find the first occurence and second is to find the last occurence of target.
    To find the first occurence of the target:
    1. Find the middle element of the list
    2. If it matches targer number, check whether the previous element of the middle element
        matches the target.
    3. It the previous element matches the target, search the first half of the list.
    4. It the previous element doesn't match the target, return the middle position as
        the first occurence of the target in the list.
    3. If the middle element is less than the target number, then search the first half of the list.
    4. If the middle element is more than the target number, then search the second half of the list.
    5. Repeat till the end of the list.
    5. If no more elements remain, return -1.
'''

from typing import List

##### Create an empty list for storing our test cases
tests = []
# Test case 01: target occurs somewhere in the middle of the array nums
tests.append({
    'input': {
        'nums': [5,7,7,8,8,10],
        'target': 8
    },
    'output': [3,4]
})
# Test case 02: target does not occur in the array nums
tests.append({
    'input': {
        'nums': [5,7,7,8,8,10],
        'target': 6
    },
    'output': [-1,-1]
})
# Test case 03: the array nums is empty
tests.append({
    'input': {
        'nums': [],
        'target': 0
    },
    'output': [-1,-1]
})
# Test case 04: target occurs once in the array nums which only has one element
tests.append({
    'input': {
        'nums': [6],
        'target': 6
    },
    'output': [0,0]
})
# Test case 05: target occurs in the beginning of the array nums
tests.append({
    'input': {
        'nums': [6,6,6,7,9,12,14],
        'target': 6
    },
    'output': [0,2]
})
# Test case 06: target occurs from the beginning to the end of the array nums
tests.append({
    'input': {
        'nums': [4,4,4,4,4,4],
        'target': 4
    },
    'output': [0,5]
})
# Test case 07: target occurs at the end of the array nums
tests.append({
    'input': {
        'nums': [6,6,6,7,9,12,14,14,14,14],
        'target': 14
    },
    'output': [6,9]
})
# Test case 08: target occurs at the end of the array nums
tests.append({
    'input': {
        'nums': [6,6,6,7,9,12,14],
        'target': 14
    },
    'output': [6,6]
})



class Solution:
    ##### Linear Search Algorithm _ Option 01 (my idea) 
    '''
    Step 3: Solution
            Linear Search Algorithm
        1. Create a variable "start" with value 0
                  a variale "end" with value 0
        2. Check whether the number at index "start" in nums equals target
        3. a. If it does, "start" and "end" are the answers for starting and ending position
           b. Check whether the number at index "end+1" in nums equals target
           c. If it does, increment the value of end by 1. Repeat step 3b.
           d. If it not, return "start" and "end".
        4. If not, return -1
    '''
    def searchRange_01 (self, nums: List[int], target: int) -> List[int]:
        start, end = 0, 0
        
        while end < len(nums):
            if nums[start] == target:
                while end+1 < len(nums) and nums[end+1] == target:
                    end += 1
                return [start,end]
            else:
                start += 1
                end += 1
        return [-1,-1]
    

    ##### Binary Search Algorithm _ Option 02 (my idea)
    '''
    Step 6: Apply the right technique to overcome inefficiency. Repeat step 3-5.
        Binary Search Algorithm - O(logn)
    We will use binary search twice.
    One is to find the first occurence and second is to find the last occurence of target.
    To find the first occurence of the target:
    1. Find the middle element of the list
    2. If it matches targer number, check whether the previous element of the middle element
        matches the target.
    3. It the previous element matches the target, search the first half of the list.
    4. It the previous element doesn't match the target, return the middle position as
        the first occurence of the target in the list.
    3. If the middle element is less than the target number, then search the first half of the list.
    4. If the middle element is more than the target number, then search the second half of the list.
    5. Repeat till the end of the list.
    5. If no more elements remain, return -1.
    '''
    def searchRange_02 (self, nums: List[int], target: int) -> List[int]:
        def first_position (nums, target):
            lo, hi = 0, len(nums) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    if mid-1 >= 0 and nums[mid-1] == target:
                        hi = mid -1
                    else:
                        return mid
                elif nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
            return -1
            
        def last_position (nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    if mid+1 < len(nums) and nums[mid+1] == target:
                        lo = mid + 1
                    else:
                        return mid
                elif nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
            return -1
    
        return [first_position(nums, target), last_position(nums, target)]



##### Test my function
test_object = Solution()
caseNumber = 0
for key in tests:
    print(f"Test case {caseNumber}: {key}")
    result = test_object.searchRange_02(**key['input']) == key['output']
    print(f" {result}")    
    caseNumber += 1
