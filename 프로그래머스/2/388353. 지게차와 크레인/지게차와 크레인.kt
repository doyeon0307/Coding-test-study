class Solution {
    fun jige(map: Array<CharArray>, c: Char, n: Int, m: Int, remove: MutableList<Pair<Int, Int>>) {
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (map[i][j] == c) {
                    if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
                        remove.add(Pair(i, j))
                    } else {
                        val visited = Array(n) { BooleanArray(m) }
                        val stack = ArrayDeque<Pair<Int, Int>>()
                        
                        stack.addLast(Pair(i, j))
                        
                        while (stack.isNotEmpty()) {
                            val last = stack.removeLast()
                            val x = last.first
                            val y = last.second

                            if (x < 0 || x >= n || y < 0 || y >= m) {
                                remove.add(Pair(i, j))
                                break
                            }
                            
                            if (!visited[x][y]) {
                                visited[x][y] = true
                                if (x - 1 < 0 || x - 1 >= 0 && map[x - 1][y] == ' ') { stack.addLast(Pair(x - 1, y))}
                                
                                if (x + 1 >= n || x + 1 < n && map[x + 1][y] == ' ') { stack.addLast(Pair(x + 1, y)) }
                                if (y - 1 < 0 || y - 1 >= 0 && map[x][y - 1] == ' ') { stack.addLast(Pair(x, y - 1)) }
                                if (y + 1 >= m || y + 1 < m && map[x][y + 1] == ' ') { stack.addLast(Pair(x, y + 1)) }
                            }
                        }
                    }
                }
            }
        }
    }
    
    fun crain(map: Array<CharArray>, c: Char, n: Int, m: Int) {
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (map[i][j] == c) { map[i][j] = ' ' }
            }
        }
    }
    
    fun solution(storage: Array<String>, requests: Array<String>): Int {
        var answer: Int = 0
        
        val n = storage.size
        val m = storage[0].length
        
        val map = Array(n) { CharArray(m) }
        
        for (i in 0 until n) {
            for (j in 0 until m) {
                map[i][j] = storage[i][j]
            }
        }
        
        for (r in requests) {
            val remove = mutableListOf<Pair<Int, Int>>()
            when (r.length) {
                1 -> {
                    jige(map, r[0], n, m, remove)
                    for (p in remove) {
                        map[p.first][p.second] = ' '
                    }
                }
                2 -> crain(map, r[0], n, m)
            }
        }
        
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (map[i][j] != ' ') { answer++ }
            }
        }
        
        return answer
    }
}