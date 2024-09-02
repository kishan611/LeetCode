class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        int len=chalk.length;
        long tot=0;
        for(int i: chalk){
            tot+=i;
        }
        k%=tot;
        for(int i=0;i<len;i++){
            if(k<chalk[i]){
                return i;
            }
            k-=chalk[i];
        }
        return 0;
    }
}