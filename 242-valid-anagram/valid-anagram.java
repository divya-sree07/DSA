import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character, Integer> hashMap = new HashMap<>();

        if (s.length() != t.length()) {
            return false;
        }

        for (char ch : t.toCharArray()) {
            if (hashMap.containsKey(ch)) {
                hashMap.put(ch, hashMap.get(ch) + 1);
            } else {
                hashMap.put(ch, 1);
            }
        }

        for (char ch : s.toCharArray()) {
            if (hashMap.containsKey(ch)) {
                hashMap.put(ch, hashMap.get(ch) - 1);
            } else {
                return false;
            }
        }

        for (char ch : hashMap.keySet()) {
            if (hashMap.get(ch) != 0) {
                return false;
            }
        }

        return true;
    }
}