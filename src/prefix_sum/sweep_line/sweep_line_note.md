# Sweep line problem

1. use map to count the interval start slot and end slot
2. when enter a new interval, map[index+1] + 1
3. when exit the interval, map[index] - 1
4. so it's IMPORTANT to sort the map by key, the sequence matter the final result
5. traverse the map sorted items and find out when we have the max count and its corresponding index.
6. 