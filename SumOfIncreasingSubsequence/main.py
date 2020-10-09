'''
Sum of largest increasing subsequence
'''
def calc_sum(array):
    dp = [0 for i in array]

    result = 0
    for i,val in enumerate(array):
         
        for j in range(i):
            if array[j]<val and dp[j]>dp[i]:
                dp[i] = dp[j]
        
        dp[i] += val
        result = max(result,dp[i])
    return result
        
if __name__ == "__main__":
    array = [1, 101, 2, 3, 100, 4, 5]
    print(calc_sum(array))
