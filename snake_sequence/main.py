def snake_sequence(array):
    dp = [[0 for i in array[0]] for j in array]
    maxi = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            up = 0
            left = 0
            if(i-1>=0 and abs(array[i-1][j]-array[i][j])==1):
                up = dp[i-1][j]
            if(j-1>=0 and abs(array[i][j-1]-array[i][j])==1):
                left = dp[i][j-1]
            dp[i][j] = max(up, left) + 1
            if(dp[i][j]>maxi):
                maxi =dp[i][j]
    return maxi

if __name__=='__main__':
    a = [[9, 6, 5, 2],[8, 7, 6, 5],[7, 3, 1, 6],[1, 1, 1, 7]]
    print(snake_sequence(a))