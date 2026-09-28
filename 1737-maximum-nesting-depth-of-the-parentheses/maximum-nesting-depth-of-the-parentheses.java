class Solution {
    public int maxDepth(String s) {
        int dp=0;
        int r=0;
        for(char ch:s.toCharArray()){
            if(ch==')'){
                dp--;
                continue;
            }
            if(ch!='(') continue;
            dp++;
            if(dp>r) r=dp;
        }
        return r;
    }
}