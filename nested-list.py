if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    bottom = 101
    secondLowest = 101
    for s in students:
        if s[1] < bottom:
            secondLowest = bottom
            bottom = s[1]

        elif s[1] < secondLowest and s[1] > bottom:
            secondLowest = s[1]

    ans = sorted([s[0] for s in students if s[1] == secondLowest])
    for name in ans:
        print(name)
    