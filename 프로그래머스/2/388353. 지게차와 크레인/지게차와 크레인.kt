class Solution {
    fun jige(map: Array<CharArray>, c: Char, n: Int, m: Int, remove: MutableList<Pair<Int, Int>>) {
        val visited = Array(n) { BooleanArray(m) }
        val bfs = ArrayDeque<Pair<Int, Int>>()
        bfs.addLast(Pair(0, 0))
        
        while (bfs.isNotEmpty()) {
            val last = bfs.removeFirst()
            val x = last.first
            val y = last.second
                        
            if (!visited[x][y]) {
                visited[x][y] = true
                
                if (x - 1 >= 0) {
                    if (map[x - 1][y] == ' ') bfs.addLast(Pair(x - 1, y))
                    if (map[x - 1][y] == c) remove.add(Pair(x - 1, y))
                }
                    
                if (x + 1 < n) {
                    if (map[x + 1][y] == ' ') bfs.addLast(Pair(x + 1, y))
                    if (map[x + 1][y] == c) remove.add(Pair(x + 1, y))
                }
                    
                if (y - 1 >= 0) {
                    if (map[x][y - 1] == ' ') bfs.addLast(Pair(x, y - 1))
                    if (map[x][y - 1] == c) remove.add(Pair(x, y - 1))
                }
                    
                if (y + 1 < m) {
                    if (map[x][y + 1] == ' ') bfs.addLast(Pair(x, y + 1))
                    if (map[x][y + 1] == c) remove.add(Pair(x, y + 1))
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
        
        val n = storage.size + 2
        val m = storage[0].length + 2
        
        val map = Array(n) { CharArray(m) { ' ' } }
        
        for (i in 0 until n - 2) {
            for (j in 0 until m - 2) {
                map[i + 1][j + 1] = storage[i][j]
            }
        }
        
        for (r in requests) {
            when (r.length) {
                1 -> {
                    val remove = mutableListOf<Pair<Int, Int>>()
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