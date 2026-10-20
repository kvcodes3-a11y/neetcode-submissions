class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = sorted(s)
        tq = sorted(t)
        if(len(tq) != len(st)):
            return False
        for i in range(len(st)):
            if(st[i] != tq[i]):
                return False
        return True