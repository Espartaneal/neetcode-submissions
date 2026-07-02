class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mydicts = {}
        mydictt = {}
        
        for letters in s:
            mydicts[letters] = mydicts.get(letters, 0) + 1
        for letters in t:
            mydictt[letters] = mydictt.get(letters, 0) + 1
            
        for keys in mydicts:
            if mydicts[keys] != mydictt.get(keys, 0):
                return False
                
        return True





        