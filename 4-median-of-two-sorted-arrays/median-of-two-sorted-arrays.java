class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0;
        int j = 0;  

        List<Integer> li = new ArrayList<>();

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j]) {
                li.add(nums1[i]);
                i++;
            } else {
                li.add(nums2[j]);
                j++;
            } 
        }

        while (i < nums1.length) {
            li.add(nums1[i]);
            i++;
        }

        while (j < nums2.length) {
            li.add(nums2[j]);
            j++;
        }
        int len = li.size();
        if (len % 2 == 0) {
            return (li.get(len/2) + li.get((len/2) - 1))/2.0;
        } else {
            return li.get(len/2);
        }
        
    }   
}