def longest_common_subset(string1,string2):
    # dp = [[[0] for i in string1] for j in string2]
    result = ""
    dp1 = [True for i in string1]
    dp2 = [True for i in string2]
    for i in range(len(string1)):
        for j in range(len(string2)):
            if(string1[i] == string2[j] and dp1[i] and dp2[j]):
                result+=string1[i]
                dp1[i]=False
                dp2[j]=False
    return result


if __name__ == "__main__":
    print(longest_common_subset('AGGTAB','GXTXAYB'))