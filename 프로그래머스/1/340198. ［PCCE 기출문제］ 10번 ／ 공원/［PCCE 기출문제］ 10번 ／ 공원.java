import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int max_size = 0;
        String empty = "-1";
        int n = park.length;
        int m = park[0].length;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (park[i][j].equals(empty)) {
                    int s = 1;
                    while (i + s < n && j + s < m) {
                        boolean can_expand = true;
                        for (int k = i; k <= i + s; k++) {
                            if (!can_expand) { break; }
                            for (int l = j; l <= j + s; l++) {
                                if (!park[k][l].equals(empty)) {
                                    can_expand = false;
                                    break;
                                }
                            }
                        }
                        if (can_expand) { s++; }
                        else { break; }
                    }
                    max_size = Math.max(s, max_size);
                }
            }
        }

        Integer[] new_mats = Arrays.stream(mats).boxed().toArray(Integer[]::new);
        Arrays.sort(new_mats, Collections.reverseOrder());
        for (Integer mat : new_mats) {
            if (mat <= max_size) { return mat; }
        }
        
        return -1;
    }
}