class Solution {
    public boolean isPalindrome(String s) {
        char[] arr = new char[s.length()];
        int k = 0;
     for (int i = 0; i < s.length(); i++) {
        if (!Character.isLetterOrDigit(s.charAt(i))){
            continue;
        }

        arr[k] = Character.toLowerCase(s.charAt(i));
        k++;
     }
        String value = new String(arr, 0, k);

        String reverse = "";
        for (int j = value.length() - 1; j >= 0;j--) {
            reverse = reverse + value.charAt(j);
        }

        return value.equals(reverse);
    }
}