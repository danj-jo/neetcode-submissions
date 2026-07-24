class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = sorted(s.upper())
        t_set = sorted(t.upper())

        print(s_set)
        print(t_set)
        counter = 0
        result = 0
        if(len(s) != len(t)):
            return False
        
        while counter < len(s):
            if(s_set[counter] == t_set[counter]):
                result = 1
                counter+=1
            else:
                result = -1
                break    
        if(result == 1):
            return True
        else: 
            return False           