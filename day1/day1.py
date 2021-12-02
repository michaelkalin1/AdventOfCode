def main():
    part_one()
    part_two()


def part_one():
    depths = []
    num_increases = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            depths.append(int(line.strip()))

    prev_depth = depths[0]
    for depth in depths[1:]:
        if depth > prev_depth:
            num_increases += 1
        prev_depth = depth

    print(num_increases)


def part_two():
    depths = []
    window_sums = []
    num_increases = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            depths.append(int(line.strip()))

    for i, depth in enumerate(depths[1:-1], start = 1):
        window_sums.append(depths[i-1] + depths[i] + depths[i+1])
    
    prev_sum = window_sums[0]
    for sum in window_sums[1:]:
        if sum > prev_sum:
            num_increases += 1
        prev_sum = sum

    print(num_increases)


if __name__ == '__main__':
    main()