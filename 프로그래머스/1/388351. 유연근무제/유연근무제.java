import java.util.*;

class Solution {    
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int today = startday % 7;
        int n = schedules.length;
        boolean[] success = new boolean[n];
        Arrays.fill(success, true);

        for (int i = 0; i < n; i++) {
            int s_t = schedules[i] / 100;
            int s_m = schedules[i] - (s_t * 100) + 10;

            if (s_m >= 60) {
                s_m -= 60;
                s_t += 1;
            }
            
            schedules[i] = s_t % 24 * 100 + s_m;
        }
                
        for (int i = 0; i < timelogs[0].length; i++) {
            if (today == 6 || today == 0) {
                today = (today + 1) % 7;
                continue;
            }
            
            for (int j = 0; j < n; j++) {
                if (schedules[j] < timelogs[j][i]) {
                    success[j] = false;
                }
            }
            
            today = (today + 1) % 7;
        }
        
        for (boolean s : success) {
            if (s) { answer++; }
        }

        return answer;
    }
}