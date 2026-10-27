# Concept here was that we need the range of the first string.
# Then we need to iterate through as long as there is a value in the next str.
#  Following that we need to confirm that the string values are the same, if they aren't we return what we can.
#  However if it passes that check, then we need to get the value and add it to the output.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        output = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return output
            output += strs[0][i]
        return output
    