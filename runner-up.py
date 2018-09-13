if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

top = -101
runnerUp = -101
for i in arr:
    if i > top:
        runnerUp = top
        top = i
        print('top: ', top)
        print('runner up : ', runnerUp)
    elif i > runnerUp and i < top:
        runnerUp = i
        print('runner up : ', runnerUp)

print(runnerUp)
