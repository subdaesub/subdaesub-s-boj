import sys
input = sys.stdin.readline

while True:
    try:
        target, guess = map(str, input().split())
        l = len(target)
        target_check = [False for _ in range(l)]
        guess_check = [False for _ in range(l)]
    
        black, grey, white = 0, 0, 0

        for i in range(l):
            if target[i] == guess[i]:
                target_check[i] = True
                guess_check[i] = True
                black += 1
        
        if target[0] == guess[1] and not target_check[0] and not guess_check[1]:
            grey += 1
            target_check[0] = True
            guess_check[1] = True
        
        if target[l - 1] == guess[l - 2] and not target_check[l - 1] and not guess_check[l - 2]:
            grey += 1
            target_check[l - 1] = True
            guess_check[l - 2] = True

        for i in range(1, l - 1):
            if target[i] == guess[i - 1] and not target_check[i] and not guess_check[i - 1]:
                grey += 1
                target_check[i] = True
                guess_check[i - 1] = True
            elif target[i] == guess[i + 1] and not target_check[i] and not guess_check[i + 1]:
                grey += 1
                target_check[i] = True
                guess_check[i + 1] = True
        
        for i in range(l):
            for j in range(l):
                if target[i] == guess[j] and not target_check[i] and not guess_check[j]:
                    white += 1
                    target_check[i] = True
                    guess_check[j] = True

        print(f'{guess}: {black} black, {grey} grey, {white} white')

    except ValueError:
        break