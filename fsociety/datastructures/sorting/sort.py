def selection_sort(input):
    print("Executing selection sort")
    for i in range(0, len(input) - 1):
        for j in range(i + 1, len(input)):
            swap(i, input, j)
    print("Completed executing selection sort")


def swap(i, input, j):
    if input[i] > input[j]:
        temp = input[i]
        input[i] = input[j]
        input[j] = temp


def insertion_sort(input):
    print("Executing insertion sort")


def merge_sort(input):
    print("Executing insertion sort")


def quick_sort(input):
    print("Executing count sort")


def count_sort(input):
    print("Executing count sort")


if __name__ == '__main__':
    data = [5, 4556, 3, -1, -9]
    selection_sort(data)
    print(data)
    float()
