class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()  # Dictionary to store frequency, first occurrence, and last occurrence of each number

        for i, num in enumerate(nums):  # Iterate through the array with index and value
            if num in mp:  # If the number is already in the dictionary
                mp[num][0] += 1  # Increment the frequency count
                mp[num][2] = i  # Update the last occurrence index
            else:
                mp[num] = [1, i, i]  # Initialize frequency to 1, and set both first and last occurrence to the current index
        
        maxCnt = minLen = 0  # Initialize maximum frequency and minimum length of subarray
        for cnt, left, right in mp.values():  # Iterate through the values in the dictionary
            if maxCnt < cnt:  # If the current frequency is greater than the maximum frequency
                maxCnt = cnt  # Update the maximum frequency
                minLen = right - left + 1  # Update the minimum length of subarray
            elif maxCnt == cnt:  # If the current frequency is equal to the maximum frequency
                if minLen > (newLen := right - left + 1):  # Calculate the new length and compare with the current minimum length
                    minLen = newLen  # Update the minimum length if the new length is smaller

        return minLen  # Return the minimum length of subarray with the maximum frequency