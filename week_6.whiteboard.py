########################## WEEK 6 DAY 1 ##########################

# Find Middle Number
# Given a number (n) and an array of numbers (num_list) as input to a function, return True if the number is greater than the middle number of the array. 
# Return False if the number is less than the middle number of the array.

# Example Input: n = 6, array = [3,5,8, 10]
# Example Output: False
# Example Input: n = 105, array = [10,30,44,22,100]
# Example Output: True

# take the array and find the len
# find the middle index
# compare the n to the middle number

def compare_n_to_middle (n, n_list):

    middle = len(n_list) // 2
    middle_number = n_list[middle]

    if n > middle_number:
        return True
    else:
        return False

def n_in_the_middle (n, n_list):
    
    return n > n_list[len(n_list) // 2]

n, array = 6, [3,5,8, 10]
n2, array2 = 105, [10,30,44,22,100]

print("\nDay 1 whiteboard")
print(compare_n_to_middle(n, array))
print(n_in_the_middle(n2, array2))


########################## WEEK 6 DAY 2 ##########################

# Lucky Numbers
# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.


def lucky_lucky(arr):

    # Initialize a dictionary to store frequencies of each integer
    freq = {}
    
    # Count the frequency of each integer in arr
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Initialize maxLucky to -1 (assumes no lucky integer by default)
    maxLucky = -1
    
    # Identify and find the largest lucky integer
    for num, count in freq.items():
        if num == count:
            maxLucky = max(maxLucky, num)
    
    # Return the largest lucky integer, or -1 if there is none
    return maxLucky

def findLucky(arr):
    freq = {}
    lucky = []
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] == num:
            lucky.append(num)
        elif freq[num] in lucky:
            lucky.remove(freq[num])
    return max(lucky, default=-1)

def findLuckyLucky(arr):
    return max([num for num in set(arr) if arr.count(num) == num], default=-1)

arr = [2,2,3,4]
arr2 = [1,2,2,3,3,3]
arr3 = [1,2,2,2,3,3,4,4,4]
arr4 = [1,1,2,3,4]

print("\nDay 2 Whiteboard")
print(lucky_lucky(arr))
print(findLucky(arr2))
print(findLuckyLucky(arr3))
print(lucky_lucky(arr4))

########################## WEEK 6 DAY 3 ##########################

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.
# This needs to be done without using the .index() or .find() built-in function. 

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def needle_in_haystack(haystack, needle):
    # Calculate lengths once for efficiency
    haystack_length = len(haystack)
    needle_length = len(needle)
    
    # If needle is empty, conventionally return 0
    if needle_length == 0:
        return 0
    
    # Iterate through haystack
    for i in range(haystack_length - needle_length + 1):
        # Check if the substring matches needle
        if haystack[i:i+needle_length] == needle:
            return i  # Return the index where match starts
    
    return -1  # Return -1 if no match is found

def findNeedle(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if all(haystack[i+j] == needle[j] for j in range(len(needle))):
            return i
    return -1

haystack, needle = "sadbutsad", "sad"
haystack1, needle1 = "goingmerrybemerry", "merry"
haystack2, needle2 = "whatisupup", "up"

print("\nDay 3 Whiteboard")
print(needle_in_haystack(haystack2, needle2))
print(findNeedle(haystack, needle))

########################## WEEK 6 DAY 4 ##########################

# TwoSum Problem

# Given an array of integers, return the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element

# arr = [5, 1, 3, 9, 10, 6]
# target = 10
# output 1, 9

# arr = [7, 1, 4, 8, 9, 11]
# target = 11
# output 7, 4

arr = [5, 1, 3, 9, 10, 6]
target = 10
arr2 = [7, 1, 4, 8, 9, 11]
target2 = 11

def two_sum(arr, target):
    
    sum = {}

    for i, current_element in enumerate(arr):
        diff = target - current_element

        if diff in sum:
            return [arr[sum[diff]], current_element]
            
        sum[current_element] = i

    return None


def sum_pairs(arr, target):
    
    sum_set = set()
    
    for i in arr:
        if target - i in sum_set:
            return [target - i, i]
        
        sum_set.add(i)

print("\nDay 4 Whiteboard")
print(two_sum(arr, target))
print(sum_pairs(arr2, target2))
