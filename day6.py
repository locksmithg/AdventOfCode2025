
def day6_part1(input):
    # operators is last line of input
    operators = input.splitlines()[-1].split()
    print(operators)
    sums = input.splitlines()[0].split()
    sums = [int(x) for x in sums]
    #print(sums)
    for line in input.splitlines()[1:-1]:
        nums = line.split()
        nums = [int(x) for x in nums]
        print(len(nums))
        c=0
        for n in nums:
            op = operators[c]
            if op == "+":
                # print(sums[c], "+", n)
                sums[c] += n
            elif op == "*":
                sums[c] *= n
            c+=1
    
    # sum all values in sums
    total = sum(sums)
    print(total)

def day6_part2(input):
    total = 0
    lines = input.splitlines()[:-1]
    ops = input.splitlines()[-1].split()
    length = len(lines[0])
    
    nums = list()
    for i in range(length):
        num = list()
        for j in range(len(lines)):
            if lines[j][i] != " ":
                num.append(lines[j][i])
        #print(num)
        if len(num) != 0:
            number = int("".join(num))
            nums.append(number)
        # if num is empty or at end of line
        if len(num) == 0 or i == length - 1:
            op = ops.pop(0)
            print(total,op,nums)
            if op == "+":
                
                total += sum(nums)
            elif op == "*":
                prod = 1
                for n in nums:
                    prod *= n
                total += prod
            nums = list()

    
    print(total)
        


if __name__ == "__main__":
    input_data = open("input6.txt").read()
    day6_part2(input_data)