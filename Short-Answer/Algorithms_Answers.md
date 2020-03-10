#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I believe it would be O(n) as the input grows linearly


b) O(n^2) both loops grow relative to N, and we have a nested loop which will
    square the amount of operations


c) O(n) with n beings the value of Bunnies is called from Bunnies-1 until reaching 0

## Exercise II

The most straight forward approach would be to drop an egg for each floor but this would
not be optimal and would drop too many eggs. We just run a basic binary search
start with the nth / 2 floor if it doesnt crack go up if does crack we go down. We
would cut the search in half as needed. 

Time complexity is O(log n)

