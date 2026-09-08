class Solution {
    public int countCommas(int n) {
        if (n < 1000) return 0;
        int start = 1000;
        int end = n;

        int count = 0;
        for (int i = start;i <= n;i++) {
            String val = String.valueOf(i);
            count += (val.length() - 1)/3;
        }

        return count;
    }
}