def lrs(string):
    result = ""
    dp = dict()
    for i in string:
        if i in dp:
            dp[i]+=1
        else:
            dp[i] = 1
        
        if(dp[i]==2):
            result+=i
            dp[i]=0
    return result

if __name__=="__main__":
    a = "aabebcdd"
    print(lrs(a))