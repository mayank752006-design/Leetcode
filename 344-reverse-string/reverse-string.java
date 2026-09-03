class Solution {
    public void reverseString(char[] s) {
        char temp;

        int l = 0;
        int h = s.length - 1;

        while (l < h) {

            temp= s[l];
            s[l] = s[h];
            s[h] = temp;

            l++;
            h--;
        }
    }
}