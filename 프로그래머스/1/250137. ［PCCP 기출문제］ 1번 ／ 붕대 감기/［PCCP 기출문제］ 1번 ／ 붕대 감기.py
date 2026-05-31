def solution(bandage, health, attacks):    
    t, x, y = map(int, bandage)

    h = health
    cur = 0
    ct = 0
    na = 0
    while True:
        cur += 1
        if attacks[na][0] == cur:
            h -= attacks[na][1]
            ct = 0
            if h <= 0:
                return -1
            na += 1
            if na >= len(attacks):
                return h
        else:
            h = min(health, h + x)
            ct += 1
            if ct >= t:
                h = min(health, h + y)
                ct = 0
    return 0