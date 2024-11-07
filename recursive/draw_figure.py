def draw_figure(n, m):
    if n <= 0:
        return
    print(' ' * m, end='')
    print('*' * n)
    draw_figure(n - 2, m +1)
    print(' ' * m, end='')
    print('#' * n)
n = int(input())
draw_figure(n, 0)