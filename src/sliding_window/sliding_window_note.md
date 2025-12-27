# Left and right pointers, which move first matters

The real decision: what do you do when the window is “invalid”?

If invalid means “too much stuff” (too many distinct, sum too big, freq too high)
→ shrink (left++) until valid.

If invalid means “not enough yet” (haven’t covered all chars, sum too small)
→ you generally expand (right++) to try to become valid.

So:

Need more to satisfy → move right

Need less to satisfy → move left


# key of sliding window 

1. Find out the condition when to switch the movement between left and right
2. Fixed window size only need 1 loop. Dynamic window size need another loop for left
3. Usually 


# Quick mental shortcut

If the problem says:

“longest … with at most …” → Template A

“minimum … that contains/at least …” → Template B

“number of subarrays/substrings with at most …” → Template C

fixed window size k → simple rolling window (or deque if max/min)

# It could be sliding window expend to both sides from the middle

# The main idea to construct a sliding window

1. the post pointer keep moving forward, new item join into the condition
2. the condition breaks, so keep moving forward the pre pointer, remove the most left item from the condition,
try resolve the condition again
3. the condition is either sum, diff, window size, count by map etc.