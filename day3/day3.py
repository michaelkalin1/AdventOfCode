def main():
    part_one()
    part_two()


def part_one():
    gamma = []
    epsilon = []
    diagnostic = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()

        diagnostic = [[char for char in line.strip()] for line in lines]

    

def part_two():
    pass


if __name__ == '__main__':
    main()