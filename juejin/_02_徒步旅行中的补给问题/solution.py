def solution(n, k, data):
    dp = [[float('inf') for _ in range(k)]for _ in range(n+1)]
    dp[0][0] = 0
    for  i in range(n):
        for j in range(k):       
            for m in range(k-j+1):
                if j - 1 <0 and m == 0:
                    continue
                else:
                    dp[i+1][j-1+m] = min([dp[i+1][j-1+m],dp[i][j] + m*data[i]])
    return min(dp[-1])


if __name__ == "__main__":
    # Add your test cases here

    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)
    print(solution(6, 3, [4, 1, 5, 2, 1, 3]) == 9)
