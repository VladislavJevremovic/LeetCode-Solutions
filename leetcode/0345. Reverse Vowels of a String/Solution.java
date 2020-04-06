// https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
    
    public String reverseVowels(String s) {
        if (s.length() <= 1) {
            return s;
        }

        int i = 0;
        int j = s.length() - 1;

        char[] chars = s.toCharArray();

        while (i < j) {
            char a = chars[i];
            char b = chars[j];

            if (!isVowel(a)) {
                i++;
                continue;
            }

            if (!isVowel(b)) {
                j--;
                continue;
            }

            char t = a;
            chars[i]= b;
            chars[j]= t;

            i++;
            j--;
        }


        return String.copyValueOf(chars);
    }
}
