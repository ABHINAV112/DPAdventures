import numpy as np
def calculate_smallest_set(array,target):
    '''
    function to calculate smallest set of indexes whose numbers add up to the target
    '''
    sort_arr_ind = sorted(enumerate(array),key=lambda x:x[1])
    sort_arr =sorted(array)
    dp = [[[len(array)+1,[]] for j in range(len(array))] for i in range(target)]
    for i in range(len(sort_arr)):
        if(sort_arr[i]<=target):
            dp[sort_arr[i]-1][i] = [1,[i]]

    # iterating through the sums
    for i in range(len(dp)):
        # iterating through the array elements
        curr_sum = i+1
        for j in range(len(dp[i])):
            curr_arr_ele = sort_arr[j]
            if curr_arr_ele>=curr_sum:
                break
            sub_prob_sum = curr_sum - curr_arr_ele
            sub_prob_sum_ind = sub_prob_sum - 1
            sub_prob_seq = dp[sub_prob_sum_ind][:j]
            if(len(sub_prob_seq)>0):
                min_val = min(sub_prob_seq,key=lambda x:x[0])
                dp[i][j]= [min_val[0]+1,min_val[1]+[j]]
    
    sort_indexes =  min(dp[target-1],key=lambda x:x[0])[1]
    result = []
    for i in sort_indexes:
        result.append(sort_arr_ind[i][0])
    return result


if __name__ == '__main__':
    array = [1,2,6,3,17,82,23,234]
    target = 26
    print(calculate_smallest_set(array,target))

    array = [1,2,6,3,17,82,23,234]
    target = 40
    print(calculate_smallest_set(array,target))

    array = [1,2,6,3,17,82,23,234] 
    target = 23
    print(calculate_smallest_set(array,target))