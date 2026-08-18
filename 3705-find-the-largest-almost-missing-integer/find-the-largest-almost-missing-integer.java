class Solution {
    public int largestInteger(int[] nums, int k) {
        int cnt[] = new int[51];
        for(int i=0;i<=nums.length-k;i++){
            boolean[] b = new boolean[51];
            for(int j=i;j<i+k;j++){
                b[nums[j]]=true;
            }
            for(int x=0;x<=50;x++){
                if(b[x]){
                    cnt[x]++;
                }
            }
        }
        for(int i=50;i>=0;i-- ){
            if(cnt[i]==1)
            return i;
        }
        return -1;
    }
}