from typing import List


def quick_sort(data: List[int], i_left:int , i_right:int):
    if i_left >= i_right:
        return

    i_split = split(data, i_left, i_right)
    quick_sort(data, i_left, i_split-1)
    quick_sort(data, i_split+1, i_right)


def split(data, i_left: int, i_right: int):
    i_mid = i_left
    i_left += 1
    while i_right >= i_left:
        while i_left <= i_right and data[i_left] <= data[i_mid]:
            i_left += 1
        while i_right >= i_left and data[i_right] >= data[i_mid]:
            i_right -= 1
        if i_right >= i_left:
            tmp = data[i_left]
            data[i_left] = data[i_right]
            data[i_right] = tmp

    # i_right is a mid index
    # move mid value to mid index.
    tmp = data[i_right]
    data[i_right] = data[i_mid]
    data[i_mid] = tmp
    return i_right


if __name__ == "__main__":
    unsorted = [5,2,9,4,0,3,1]
    print(unsorted)
    quick_sort(unsorted, 0, len(unsorted)-1)
    print(unsorted)