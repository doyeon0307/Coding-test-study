import java.util.List;
import java.util.ArrayList;

class Solution {
    public boolean is_spoiler(int start, int end, int[][] spoiler_ranges) {
        for (int[] s : spoiler_ranges) {
            if (start <= s[1] && end >= s[0]) {
                return true;
            }
        }
        return false;
    }
    
    public int solution(String message, int[][] spoiler_ranges) {      
        List<String> secrets = new ArrayList<>();
        List<String> not_secrets = new ArrayList<>();
        
        String w = "";
        for (int i = 0; i < message.length(); i++) {
            boolean is_last = i == message.length() - 1;
            
            if (message.charAt(i) != ' ' && !is_last) {
                w += message.charAt(i);
                continue;
            }
            
            int start = i - w.length();
            int end = i - 1;
            
            if (is_last) {
                w += message.charAt(i);
                end += 1;
            }
                        
            boolean is_spoiler = is_spoiler(start, end, spoiler_ranges);
            boolean already_secrets = secrets.contains(w);

            if (is_spoiler && !already_secrets) secrets.add(w);
            if (!is_spoiler) not_secrets.add(w);
            w = "";
        }
        
        int answer = 0;
        for (String s : secrets) {
            if (!not_secrets.contains(s)) answer += 1;
        }
        
        return answer;
    }
}