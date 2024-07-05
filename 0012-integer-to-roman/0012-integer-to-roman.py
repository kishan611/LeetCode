class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        symbols=[('M','CM'),('D','CD'),('C','XC'),('L','XL'),('X','IX'),('V','IV')]
        values=[(1000,900),(500,400),(100,90),(50,40),(10,9),(5,4)]
        for i in range(6):
            res+=symbols[i][0]*(num//values[i][0])
            num%=values[i][0]
            if num>=values[i][1]:
                res+=symbols[i][1]
                num-=values[i][1]
        res+="I"*(num)
        return res
            
            
        
        