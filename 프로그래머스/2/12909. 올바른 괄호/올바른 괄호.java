import java.util.*;

class Solution {
    boolean solution(String s) {       
        ArrayDeque<Character> stack = new ArrayDeque();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (stack.isEmpty()) { stack.push(c); continue; }
            
            if (stack.peek() == '(' && c == ')') {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        
        return stack.isEmpty();
    }
}