class Solution:
    def romanToInt(self, s: str) -> int:
        
        ret = 0
        trail = ''
        target = ''
        lead = ''
        string_with_suffix = s + '~'
        
        for i in string_with_suffix:
            
            #initalize variables
            trail = target
            target = lead
            lead = i
            
            #single 1's 10's and 100's
            if target == 'I' and not lead == 'V' and not lead =='X':
                ret += 1
            if target == 'X' and not lead == 'L' and not lead =='C' and not trail == 'I':
                ret += 10
            if target == 'C' and not lead == 'D' and not lead =='M' and not trail == 'X':
                ret += 100
            
            #subtration cases
            if target == 'I' and lead =="V":
                ret += 4
            if target == 'I' and lead =="X":
                ret += 9
            
            if target == 'X' and lead =="L":
                ret += 40
            if target == 'X' and lead =="C":
                ret += 90
                
            if target == 'C' and lead =="D":
                ret += 400
            if target == 'C' and lead =="M":
                ret += 900

            
            #single 5's 50's 500's 1000's
            if target == 'V' and not trail == 'I':
                ret += 5
            if target == 'L' and not trail == 'X':
                ret += 50
            if target == 'D' and not trail == 'C':
                ret += 500
            if target == 'M' and not trail == 'C':
                ret += 1000
          
        return ret

Roman = Solution()
print(Roman.romanToInt("MCMXCIV"))