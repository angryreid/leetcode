class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)  # Dictionary to store grouped anagrams, defaulting to an empty list
        for s in strs:  # Iterate through each string in the input list
            counts = [0] * 26  # Initialize a list of 26 zeros to count occurrences of each letter
            for c in s:  # Iterate through each character in the string
                counts[ord(c) - ord('a')] += 1  # Increment the count for the corresponding letter
            key = ''.join(['#' + str(count) for count in counts])  # Create a unique key based on letter counts
                        # counts = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        # ['#1', '#2', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0', '#0']
                        # key = '#1#2#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0'
            mp[key].append(s)  # Append the string to the list corresponding to the key in the dictionary
        return list(mp.values())  # Return the grouped anagrams as a list of lists