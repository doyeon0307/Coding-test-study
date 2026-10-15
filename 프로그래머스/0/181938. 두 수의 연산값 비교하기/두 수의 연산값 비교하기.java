class Solution {
    public int solution(int a, int b) {
        int answer = Integer.valueOf(Integer.toString(a) + Integer.toString(b));
        if (answer < 2 * a * b) {
            answer = 2 * a * b;
        }
        
        return answer;
    }
}