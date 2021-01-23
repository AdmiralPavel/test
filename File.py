with open('text.txt', 'w') as f:
    for i in range(100):
        f.write(f'{i}\n')

with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')
