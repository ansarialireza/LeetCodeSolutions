
def maxSubsequence(nums,k):
    main_list = []
    row_list = []
    for i in range(0,len(nums)):
        row_list = []
        row_list.append(i)
        row_list.append(nums[i])
        main_list.append(row_list)

    main_list.sort(key=lambda x: x[1])
    new_list = main_list[-k:]
    new_list.sort(key=lambda x: x[0])
    final_list = []
    for i in range(0,len(new_list)):
        final_list.append(([new_list[i][1]].pop()))

    return final_list

nums = [3,-1,-2,4]
k = 3

output=maxSubsequence(nums,k)
print(output)
