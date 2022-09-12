"""Code for merging two sorted lists."""


def merge(x: list, y: list):
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []
    while i < len(x) and j < len(y):
        if x[i] <= y[i]:
            z.append(x[i])
            i+=1
        if x[i] >= y[j]:
            z.append(y[j])
            j+=1
        if i==len(x):
            z+=y[j:]
        if j==len(y):
            z+=x[i:]
    return z
