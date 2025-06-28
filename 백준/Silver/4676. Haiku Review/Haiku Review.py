import sys
input = sys.stdin.readline

syllables = ['a', 'e', 'i', 'o', 'u', 'y']

while True:
    s = input().strip()
    if s == 'e/o/i':
        break
    lines = list(map(str, s.split('/')))
    
    clk = False
    syllable_cnt = 0
    wrong_line = []
    
    for i in range(3):
        if i == 1:
            for j in range(len(lines[i])):
                if lines[i][j] in syllables:
                    if not clk:
                        syllable_cnt += 1
                        clk = True
                else:
                    clk = False
            
            if syllable_cnt != 7:
                wrong_line.append(i + 1)
            clk = False
            syllable_cnt = 0
                    
        else:
            for j in range(len(lines[i])):
                if lines[i][j] in syllables:
                    if not clk:
                        syllable_cnt += 1
                        clk = True
                else:
                    clk = False
            
            if syllable_cnt != 5:
                wrong_line.append(i + 1)
            clk = False
            syllable_cnt = 0
            
    if not wrong_line:
        print('Y')
    else:
        print(wrong_line[0])