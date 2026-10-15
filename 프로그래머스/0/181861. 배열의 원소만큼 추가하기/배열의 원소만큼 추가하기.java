import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        
        for (int a : arr) {
            for (int i = 0; i < a; i++) {
                answer.add(a);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}