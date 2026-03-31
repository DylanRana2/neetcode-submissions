class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        ssort = sorted(s)
        tsort = sorted(t)
        return (ssort == tsort)