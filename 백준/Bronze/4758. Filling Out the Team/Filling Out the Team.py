while True:
    speed, weight, strength = map(float, input().split())
    if speed == 0 and weight == 0 and strength == 0:
        break
    clk = True
    if speed <= 4.5 and weight >= 150 and strength >= 200:
        print("Wide Receiver", end=' ')
        clk = False
    if speed <= 6.0 and weight >= 300 and strength >= 500:
        print("Lineman", end=' ')
        clk = False
    if speed <= 5.0 and weight >= 200 and strength >= 300:
        print("Quarterback", end=' ')
        clk = False
    if clk:
        print("No positions", end=' ')
    print()