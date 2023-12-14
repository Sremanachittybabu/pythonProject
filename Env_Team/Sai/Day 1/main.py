import re

def f(line):
    for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        line = line.replace(n, n + str(i+1) + n)
        print(line)
    x = re.findall(r'(\d)', line)
    print(int(x[0] + x[-1]))
    return int(x[0] + x[-1])

print(sum(map(f, open('input2.txt'))))
