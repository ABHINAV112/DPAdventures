'''
Minimum changes to make an array strictly increasing
'''

def main(array):
    dp = [0 for i in array]
    result = 0
    for i, val in enumerate(array):
        for j in range(i):
            if val> array[j] and dp[i]<dp[j]:
                dp[i] = dp[j]
        dp[i] +=1
        result = max(dp[i],result)

    return len(array) - result


if __name__ == "__main__":
    a = [1, 2, 6, 5, 4]
    print(main(a))
