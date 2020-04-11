def size(systems):
    return len(systems)


def print_list(input):
    for data in input:
        print(data)
    for data in input:
        print(data)


if __name__ == '__main__':
    systems = ['uc', 'unix', 'osX', 'Windows', 'linux']
    print_list(systems)
    print(size(systems))
