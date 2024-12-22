# converting integer to roman
# this is my code 
class Solution:
    def intToRoman(self, num: int) -> str:
        res=[]
        res.extend(['M' for _ in range(num//1000)])
        num%=1000
        if num>=900:
            res.append("CM")
            num%=900
        else:
            res.extend(['D' for _ in range(num//500)])
            num%=500
            if num>=400:
                res.append("CD")
                num%=400
            else:
                res.extend(['C' for _ in range(num//100)])
                num%=100
        if num>=90:
            res.append("XC")
            num%=90
        else:
            res.extend(['L' for _ in range(num//50)])
            num%=50
            if num>=40:
                res.append('XL')
                num%=40
            else:
                res.extend(['X' for _ in range(num//10)])
                num%=10
        if num>=5:
            if num==9:
                res.append('IX')
                num=0
            else:
                res.extend(['V' for _ in range(num//5)])
                num%=5
        elif num==4:
            res.append('IV')
            num=0
        res.extend(['I' for _ in range(num//1)])
        return ''.join(res)
