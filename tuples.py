if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    output = tuple(integer_list)
    print(hash(output))
    