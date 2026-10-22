class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = ""
        ts = ""
        for i in s:
            if('a' <= i <= 'z' or '0' <= i <= '9'):
                st = st + i
        
        for i in st:
            ts = i + ts
        
        if(ts == st):
            return True
        else:
            return False