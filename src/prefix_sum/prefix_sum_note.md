# To sum up nums[i]

Sum[i:j] = Sum[j:0] - Sum[i:0]

Sum[i] = Sum[i-1] + nums[i-1]

so,

len(Sum) = len(nums) + 1

```
for i in range(1, n+1):
    sum_subarrays[i] = sum_subarrays[i-1] + nums[i-1]
```


!! CAN'T use the following pattern to sum up , must follow 

In this case, pre_sum contains i+1 elements, but it's stored in sum_subarrays[i]

The following case can only be used when sum_subarrays is not query by index.

 ```
 for num in nums:
     pre_sum += num
     sum_subarrays.append(pre_sum)
```