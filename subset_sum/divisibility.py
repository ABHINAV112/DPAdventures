def is_subset_sum(array,target):
    '''
    Function to check if a subset exists which adds upto a particular sum which is divisible by a value exists in the array
    '''
    '''
    3 4 1 2 , 6 -> True

    3 4 1 2
    0 0 0 0
    3 3 3 3
      4 4 4
      7 7 7
        1 1
        4 4
        5 5
        8 8
          2
          5
          6
          9
          3
          6
          7
          10
    '''
    dp = [0]
    for i in array:
        for j in range(len(dp)):
            curr_sum = dp[j]+i
            if(curr_sum%target==0):
                return True
            dp.append(curr_sum)
    return False

if __name__ == '__main__':
    arr = [1, 6]
    tar = 5
    print(is_subset_sum(arr,tar))