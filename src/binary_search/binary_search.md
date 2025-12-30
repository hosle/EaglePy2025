# Every time you see a problem that involves a sorted array, you should consider binary search.

# Binary search has two points to remember

## Calculation of mid

1. mid = (low + high ) // 2 , might cause overflow
2. mid = low + (high - low) // 2, safe for overflow, with the same result

## understanding the exact, lower bound and upper bound and their conditions

   1. Consider the duplicated elements in the array, what to do when arr[mid] == target. continue search? to right or left?

## consider the condition while (low < high) or while (low <= high), if the afterward action when equals found, should let low==high case go into the loop

## 