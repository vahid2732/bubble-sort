def asc(a, b):
    return a < b


def desc(a, b):
    return a > b


def bubble_sort(nums, order):
    n = len(nums)-1
    for i in range(n):
        for j in range(n-i):
             if order(nums[j], nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)


list1 = [21, -16, 48, 2, 113, 214,]

print('descending:\t')
bubble_sort(list1, desc)

print('ascending:\t')
bubble_sort(list1, asc)
