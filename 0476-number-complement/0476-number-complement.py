class Solution:
    def findComplement(self, num: int) -> int:
        binary=list(bin(num)[2::])
        for i in range(len(binary)):
            if binary[i]=='1':
                binary[i]='0'
            else:
                binary[i]='1'
        return int('0b'+"".join(binary),2)
        