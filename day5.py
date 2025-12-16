import intervaltree

def day5_part1(input):
    fresh = 0
    rangesEnd = False
    ranges = list()
    for line in input.splitlines():
        if line == "":
            rangesEnd = True
            continue
        if not rangesEnd:
            parts = line.split("-")
            start, end = int(parts[0]), int(parts[1])
            ranges.append((start, end))
        else:
            for r in ranges:
                if r[0] <= int(line) <= r[1]:
                    fresh += 1
                    break
    print(fresh)

def day5_part2(input):
    totalFresh = 0
    tree = intervaltree.IntervalTree()
    for line in input.splitlines():
        if line == "":
            break
        tree.add(intervaltree.Interval(int(line.split("-")[0]), int(line.split("-")[1]) + 1))
    tree.merge_overlaps(strict=False)
    ranges = sorted(tree)
    for r in ranges:
        #print(r)
        totalFresh += (r.end - r.begin)
    print(totalFresh)
    
def day5_p2_diy(input):
    totalFresh = 0
    ranges = []
    for line in input.splitlines():
        if line == "":
            break
        parts = line.split("-")
        start, end = int(parts[0]), int(parts[1])
        ranges.append([start, end])
    ranges.sort() # sort so start is ascending
    merged = []
    N = len(ranges)
    for i in range(N):
        start = ranges[i][0]
        end = ranges[i][1]

        if merged and merged[-1][1] >= end: # check for contained range
            continue

        for j in range(i + 1, N):
            if ranges[j][0] <= end:
                end = max(end, ranges[j][1])
        merged.append([start, end])
    for r in merged:
        totalFresh += (r[1] - r[0] + 1)
    print(totalFresh)


if __name__ == "__main__":
    input = open("input5.txt").read()
    day5_part1(input)
    day5_part2(input)
    day5_p2_diy(input)