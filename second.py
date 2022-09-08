class Solution:
    def romanToInt(self, s: str) -> int:
        varity={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        for i in range(len(s)):
            # sum+=varity[s[i]]
            if i>0 and s[i]=="V" and s[i-1]=="I":
                sum+=varity[s[i]]-1-varity[s[i-1]]
            elif i>0 and s[i]=="X" and s[i-1]=="I":
                sum+=varity[s[i]]-1-varity[s[i-1]]
            elif i>0 and s[i]=="L" and s[i-1]=="X":
                sum+=varity[s[i]]-10-varity[s[i-1]]
            elif i>0 and s[i]=="C" and s[i-1]=="X":
                sum+=varity[s[i]]-10-varity[s[i-1]]
            elif i>0 and s[i]=="D" and s[i-1]=="C":
                sum+=varity[s[i]]-100-varity[s[i-1]]
            elif i>0 and s[i]=="M" and s[i-1]=="C":
                sum+=varity[s[i]]-100-varity[s[i-1]]
            else:
                sum+=varity[s[i]]
        return sum