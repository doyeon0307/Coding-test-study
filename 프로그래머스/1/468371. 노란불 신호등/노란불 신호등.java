class Solution {
    public boolean is_yellow(int t, int[] s) {
        for (int i = s[0] + 1; i < s[0] + s[1] + 1; i++) {
            if ((t - i) % (s[0] + s[1] + s[2]) == 0) {
                return true;
            }
        }
        
        return false;
    }
    
    public int gcd(int x, int y) {
        return y == 0 ? x : gcd(y, x % y);
    }

    public int solution(int[][] signals) {      
        int[] s = signals[0];
        int a = s[0] + s[1] + s[2];
        int b = s[0] + 1;
        int c = s[0] + s[1];
        
        int m = 1;
        for (int[] n : signals) {
            int p = n[0] + n[1] + n[2];
            m = m / gcd(m, p) * p;
        }
        
        for (int x = 0; x <= m; x++) {
            int start = a * x + b;
            int end = a * x + c;
            
            for (int y = start; y < end + 1; y++) {
                boolean all_y = true;
                
                for (int i = 1; i < signals.length; i++) {
                    if(!is_yellow(y, signals[i])) {
                        all_y = false;
                        break;
                    }
                }
                
                if (all_y) {
                    return y;
                }
            }
        }
        
        return -1;
    }
}