def generate_vector(idx, vector, n):
    if idx >= len(vector):
        print(*vector, sep=' ')
        return
    for x in range(1, n +1):
        vector[idx] = x
        generate_vector(idx + 1, vector, n)



n = int(input())
vector = [None] * n

generate_vector(0, vector, n)