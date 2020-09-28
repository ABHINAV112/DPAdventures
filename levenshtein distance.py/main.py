def calculate_levenshtein_distance(string1, string2):
    n1 = len(string1)
    n2 = len(string2)
    dp = [[0 for j in range(n1+1)] for i in range(n2+1)]
    for i in range(n2+1):
        for j in range(n1+1):
            if i ==0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif string1[j-1]==string2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]


if __name__ == "__main__":
    str1 = "anusha"
    str2 = "abhinav"
    print(calculate_levenshtein_distance(str1,str2))

