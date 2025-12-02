import time

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

def day2_part2(input):
    sumInvalidIds = 0
    for ids in input.split(','):# for each id range
        lower = ids.strip().split('-')[0]
        upper = ids.strip().split('-')[1]
        for i in range(int(lower), int(upper)+1): # for each id in range
            iChars = str(i) # convert to string
            half = int(len(iChars)/2) # 
            for j in range(1, half+1):
                if len(iChars)%j != 0:
                    continue
                sequence = iChars[0:j]
                valid = False
                for k in range(0, len(iChars), j):
                    if iChars[k:k+len(sequence)] != sequence:
                        valid = True
                if not valid:
                    # print(i)
                    sumInvalidIds += i
                    break
    print(sumInvalidIds)

factors = [[1], [1], [1], [1,2], [1], [1,2,3], [1], [1,2,4], [1,3], [1,2,5]]
def day2_part2_factors(input):
    total = 0
    for ids in input.split(','):# for each id range
        lower = ids.strip().split('-')[0]
        upper = ids.strip().split('-')[1]
        for i in range(int(lower), int(upper)+1):
            iChars = str(i) # convert to string
            length = len(iChars)
            if length == 1:
                continue
            for f in factors[length-1]:
                c = iChars.count(iChars[0:f])
                if c == length / f:
                    total += i
                    # print(i)
                    break
    print(total)
            
if __name__ == "__main__":
    data = open("input2.txt").read()
    #day2_part1(data)
    timer = time.time()
    day2_part2(data)
    print("Time to run:", time.time() - timer)
    timer = time.time()
    day2_part2_factors(data)
    print("Time to run:", time.time() - timer)