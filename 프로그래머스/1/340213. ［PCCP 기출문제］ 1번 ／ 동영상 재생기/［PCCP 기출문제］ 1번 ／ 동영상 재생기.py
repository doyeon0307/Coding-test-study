def m_s_to_string(m, s):
    s_m = str(m)
    if len(s_m) < 2:
        s_m = "0" + s_m
    s_s = str(s)
    if len(s_s) < 2:
        s_s = "0" + s_s
    return s_m + ":" + s_s

def prev(pos):
    m, s = map(int, pos.split(":"))
    s -= 10
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        return "00:00"
    else:
        return m_s_to_string(m, s)
     
def nxt(pos, video_len):
    m, s = map(int, pos.split(":"))
    s += 10
    if s > 59:
        s -= 60
        m += 1
    return min(video_len, m_s_to_string(m, s))

def skip(pos, op_start, op_end):
    if op_start <= pos <= op_end:
        return op_end
    return pos

def solution(video_len, pos, op_start, op_end, commands):
    for c in commands:
        pos = skip(pos, op_start, op_end)
        if c == "next":
            pos = nxt(pos, video_len)
        else:
            pos = prev(pos)
        pos = skip(pos, op_start, op_end)

    return pos