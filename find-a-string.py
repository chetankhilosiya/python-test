def count_substring(string, sub_string):
    count = 0
    string_part = string
    while string_part != '':
        position = string_part.find(sub_string)
        if position != -1:
            count += 1
            string_part = string_part[position+1:]
        else:
            string_part = ''
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)