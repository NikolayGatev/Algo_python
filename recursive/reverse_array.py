def reverse_and_print(arr):
    if len(arr) > 1 and arr[-2] == '-':
        print(f'{arr.pop(-2)}{arr.pop()}', end='')
    else:
        print(arr.pop(), end='')
    if not arr:
        return
    reverse_and_print(arr)

arr = list(input())

reverse_and_print(arr)