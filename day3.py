
def day3_part1(input):
    d1 = 0
    d2 = 0
    total = 0
    for line in input.splitlines():
        d1Index = 0
        for c in range(len(line)-1):
            if int(line[c]) > d1:
                d1 = int(line[c])
                d1Index = c
        for c in range(d1Index+1, len(line)):
            if int(line[c]) > d2:
                d2 = int(line[c])
        
        total += int(f"{d1}{d2}")
        d1 = 0
        d2 = 0
    print(total)

def day3_part2(input):
    digits = list()
    total = 0
    index = 0
    for line in input.splitlines():
        freeSlots = len(line) - 12
        for i in range(12):
            choices = line[index: index + freeSlots + 1]
            maxDigit = 0
            subIndex = 0
            for j in range(len(choices)):
                if int(choices[j]) > maxDigit:
                    maxDigit = int(choices[j])
                    subIndex = j
            digits.append(str(maxDigit))
            index += subIndex + 1
            freeSlots -= subIndex
        total += int(''.join(digits))
        # print(digits)
        digits.clear()
        index = 0
            
    print(total)

if __name__ == "__main__":
    data = open("input3.txt").read()
    day3_part1(data)
    day3_part2(data)