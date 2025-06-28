t = int(input())
for i in range(t):
    gandalph = list(map(int, input().split()))
    sauron = list(map(int, input().split()))
    gandalph_score = gandalph[0] + gandalph[1] * 2 + gandalph[2] * 3 + gandalph[3] * 3 + gandalph[4] * 4 + gandalph[5] * 10
    sauron_score = sauron[0] + sauron[1] * 2 + sauron[2] * 2 + sauron[3] * 2 + sauron[4] * 3 + sauron[5] * 5 + sauron[6] * 10
    if gandalph_score > sauron_score:
        print(f"Battle {i + 1}: Good triumphs over Evil")
    elif sauron_score > gandalph_score:
        print(f"Battle {i + 1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i + 1}: No victor on this battle field")