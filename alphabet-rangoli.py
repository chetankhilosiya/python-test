def print_rangoli(size):
    max_length = 1 + 4 * (size - 1)
    print(max_length)
    for i in range(1, size + 1):
        value = ''
        for j in range(0, i):
            value += chr(97 + size - 1 - j) + '-'
        firstRun = True
        for j in range(i, 1, -1):
            if firstRun:
                value += chr(97 + size + 1 - j)
                firstRun = False
            else:
                value += '-' + chr(97 + size + 1 - j)
        print(value.center(max_length, '-'))
    
    for i in range(size, 1, -1):
        value = ''
        for j in range(1, i):
            value += chr(97 + size - j) + '-'
        firstRun = True
        for j in range(i - 2, 0, -1):
            if firstRun:
                value += chr(97 + size - j)
                firstRun = False
            else:
                value += '-' + chr(97 + size - j)
        print(value.center(max_length, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)