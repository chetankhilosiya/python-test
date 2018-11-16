(n, m) = (int(i) for i in input().split())
pattern = '.|.'
welcome = 'WELCOME'
for i in range(1, ((n-1)//2) + 1):
    patternLength = len(pattern) * (i*2 - 1)
    dashLength = (m - patternLength) // 2
    print('-'*dashLength, end='')
    print(pattern* (i*2 - 1), end='')
    print('-'*dashLength)
print('-' * ((m - len(welcome)) // 2), end='')
print(welcome, end='')
print('-' * ((m - len(welcome)) // 2))
for i in range(((n-1)//2), 0, -1):
    patternLength = len(pattern) * (i*2 - 1)
    dashLength = (m - patternLength) // 2
    print('-'*dashLength, end='')
    print(pattern* (i*2 - 1), end='')
    print('-'*dashLength)