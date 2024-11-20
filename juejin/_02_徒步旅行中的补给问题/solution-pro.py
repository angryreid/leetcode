def solution(n, k, data):
    length = len(data)
    # Create a dp array; note that we don't need to buy food on the last day
    dp = [0] * length
    # Basic case: at least one portion of food must be bought on the first day
    dp[0] = data[0]

    # Iterate: dp[i] represents the minimum cost of the journey on day i with a weight limit of k
    for i in range(1, length):
        # Directly buy food
        dp[i] = dp[i - 1] + data[i]
        # Use previously bought food
        for j in range(i - 1, max(i - k, -1), -1):
            dp[i] = min(dp[i], dp[i - 1] + data[j])

    return dp[- 1]

# Test cases
if __name__ == "__main__":
    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)
    print(solution(6, 3, [4, 1, 5, 2, 1, 3]) == 9)
    print(solution(4, 1, [3, 2, 4, 1]) == 10)
