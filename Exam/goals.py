def find_best_increasing_sequence(goals):
    n = len(goals)
    # DP array to store the length of the longest subsequence ending at each match
    dp = [1] * n
    # Parent array to track the sequence for reconstruction
    parent = [-1] * n

    # Fill the DP table
    for i in range(n):
        for j in range(i):
            if goals[j] <= goals[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find the index of the largest value in dp (this gives us the last element of the best sequence)
    max_length_index = dp.index(max(dp))

    # Reconstruct the sequence by backtracking using the parent array
    sequence = []
    while max_length_index != -1:
        sequence.append(goals[max_length_index])
        max_length_index = parent[max_length_index]

    # The sequence is constructed in reverse order, so reverse it
    sequence.reverse()

    # Return the sequence
    return sequence


# Input reading
input_goals = input().strip()
goals = list(map(int, input_goals.split(", ")))

# Find the best increasing subsequence
best_sequence = find_best_increasing_sequence(goals)

# Output the result
print(" ".join(map(str, best_sequence)))
