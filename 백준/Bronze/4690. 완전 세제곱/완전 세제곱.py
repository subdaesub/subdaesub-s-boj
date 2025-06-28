for i in range(6, 101):
    for j in range(2, i):
        for k in range(j + 1, i):
            for l in range(k + 1, i):
                if j**3 + k**3 + l**3 == i**3:
                    print(f"Cube = {i}, Triple = ({j},{k},{l})")