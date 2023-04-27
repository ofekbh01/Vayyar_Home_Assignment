"""
Rules:
> You cannot change values in the matrix
> There will be no adjacent submarines
> No more than 2 parameters

> if successful: bring a solution for a 2D submarines
"""
DD_SUB_MATRIX = [
    [1, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0]
]

D_SUB_MATRIX = [
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0]
]


def d():
    """
    searches for a start of submarine sequence, then calls func "find_whole_sub"
    counts num of submarines
    :return: number of submarines
    """
    sub_count = 0
    seen = []
    for i in range(len(DD_SUB_MATRIX)):
        for j in range(len(DD_SUB_MATRIX[0])):
            if (i, j) not in seen and DD_SUB_MATRIX[i][j] == 1:
                find_whole_sub(i, j, seen)
                sub_count += 1
    return sub_count


def find_whole_sub(i, j, seen):
    """
    takes the start of the submarine and checks saves its location (every continuous 1 value on the matrix) recursively
    :param i: the y value in the matrix
    :param j: the x value in the matrix
    :param seen: list of all 1 values locations the script went through already
    :return: none
    """
    if (i, j) in seen:
        return
    elif DD_SUB_MATRIX[i][j] == 0:
        return
    else:
        seen.append((i, j))
        if i + 1 < len(DD_SUB_MATRIX):
            find_whole_sub(i+1, j, seen)
        if j + 1 < len(DD_SUB_MATRIX[0]):
            find_whole_sub(i, j+1, seen)


if __name__ == '__main__':
    print(d())
