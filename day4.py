def day4_part1(lines):
    lines = [list(line) for line in lines]
    rows = len(lines)
    cols = len(lines[0])
    scores = [[0 for _ in range(cols)] for _ in range(rows)]
    directions = [
    (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
    (0, -1),           (0, 1),   # Left, Right
    (1, -1),  (1, 0),  (1, 1)    # Bottom-left, Bottom, Bottom-right
    ]
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '@':
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        scores[new_row][new_col] += 1
            else:
                scores[r][c] = 99
    
    # count number of cells with score < 4
    count = 0
    for r in range(rows):
        for c in range(cols):
            if scores[r][c] < 4:
                count += 1
                lines[r][c] = '.'
    #print(count)
    lines = [''.join(line) for line in lines]
    return lines, count

def day4_part2(lines):
    previous = -1
    total = 0
    while previous != total:
        previous = total
        lines, count = day4_part1(lines)
        total += count
    print(total)


if __name__ == "__main__":
    input = open("input4.txt").read()
    #day4_part1(input.splitlines())
    day4_part2(input.splitlines())