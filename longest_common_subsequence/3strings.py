def lcs(str1,str2,str3):
    dp1 = [True for i in str1]
    dp2 = [True for i in str2]
    dp3 = [True for i in str3]
    result = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            for k in range(len(str3)):
                if(str1[i] == str2[j] == str3[k] and dp1[i] and dp2[j] and dp3[k]):
                    result+=str1[i]
                    dp1[i] = False
                    dp2[j] = False
                    dp3[k] = False
    return result


if __name__ == "__main__":
    # str1 = "geeks" 
    # str2 = "geeksfor"  
    # str3 = "geeksforgeeks"
    str1 = "abcd1e2"  
    str2 = "bc12ea"  
    str3 = "bd1ea"
    print(lcs(str1, str2, str3))
