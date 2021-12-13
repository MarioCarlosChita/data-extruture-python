# from tree import TreeNode
# t = TreeNode("Electronic");
# laptops = TreeNode("LapTops")
# laptops.Add(TreeNode('Mac'))
# laptops.Add(TreeNode('Dell'))
# laptops.Add(TreeNode('HP'))
# t.Add(laptops)
# t.print_tree()


# n  = 124;
# rev= 0;
# while n  >   0:
#       rev =  (rev * 10)  +  n % 10;
#       n =n //10;
# print(rev);


def sum_array(arr, k):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    for end, val in  enumerate(arr):
        current_sum += val
        if end-start + 1 == k:
            max_sum = max(max_sum,  current_sum)
            current_sum -= arr[start]
            start += 1
    return max_sum


print(sum_array([2,3,4,1,5] ,3));


