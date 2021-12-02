def main():
    part_one()
    part_two()


def part_one():
    x = 0
    y = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            if line[0] == 'forward':
                x += int(line[1])
            elif line[0] == 'up':
                y -= int(line[1])
            elif line[0] == 'down':
                y += int(line[1])

    print(f'({x}, {y})')
    print(x*y)


def part_two():
    x = 0
    y = 0
    aim = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            if line[0] == 'forward':
                x += int(line[1])
                y += aim*int(line[1])
            elif line[0] == 'up':
                aim -= int(line[1])
            elif line[0] == 'down':
                aim += int(line[1])

    print(f'({x}, {y})')
    print(x*y)


if __name__ == '__main__':
    main()