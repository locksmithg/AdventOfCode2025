def day2_part1(input):
    sumInvalidIds = 0
    for ids in input.split(','):
        lower = ids.strip().split('-')[0]
        upper = ids.strip().split('-')[1]
        for i in range(int(lower), int(upper)+1):
            iChars = str(i)
            if len(iChars)%2 != 0:
                continue
            half = int(len(iChars)/2)
            if iChars[0: half] == iChars[half:]:
                sumInvalidIds += i
                # print(i)
    print(sumInvalidIds)


if __name__ == "__main__":
    data = open("input2.txt").read()
    day2_part1(data)
