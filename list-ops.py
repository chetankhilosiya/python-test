if __name__ == '__main__':
    N = int(input())
    output_list = []
    for i in range(N):
        command, *args = input().split()
        args = list(map(int, args))
        if (command == 'print'):
            print(output_list)
        else:
            method = getattr(output_list, command, lambda: 'invalid command')
            method(*args)
