class Solution:
    def numberToWords(self, num: int) -> str:
        words=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',"Eleven",'Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens=['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        if num==0:
            return words[0]
        def word(n):
            if len(n)==3:
                h=int(n[0])
                t=int(n[1:])
                if int(n)==0:
                    return 'Zero'
                if int(n)<20:
                    return words[int(n)]
                if h==0 and t%10!=0:
                    return tens[t//10-2]+' '+words[t%10]
                if h==0:
                    return tens[t//10-2]
                if t==0:
                    return words[h]+' Hundred'
                if t<20:
                    return words[h]+' Hundred '+words[t]
                td=n[2]
                if td=='0':
                    return words[h]+' Hundred '+tens[t//10-2]
                return words[h]+' Hundred '+tens[t//10-2]+' '+words[int(td)]
            if int(n)<20:
                return words[int(n)]
            if n[-1]=='0':
                return tens[int(n)//10-2]
            return tens[int(n)//10-2]+' '+words[int(n[-1])]
        num=str(num)[::-1]
        num=[num[i:i+3][::-1] for i in range(0,len(num),3)]
        num.reverse()
        n=len(num)
        i=0
        res=[]
        ons=['Thousand','Million','Billion']
        while i<n:
            temp=word(num[i])
            if temp!='Zero':
                if i!=n-1:
                    res+=temp.split(' ')
                    res+=[ons[n-i-2]]
                else:
                    res+=temp.split(' ')
            i+=1
        return " ".join(res)
    
