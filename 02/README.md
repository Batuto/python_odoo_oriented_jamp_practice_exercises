You must write a method for a burrito store. It must be efficient respect time, it must find the n-th lowest selling type of burrito, with that burrito's id. The n-th lowest selling burrito is the burrito that has more sales than n-1 burrito. If multiple burritos share the n-th lowest selling spot, the method can return any one of them.

For example,
 nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2)
should return 2. In the list, the burrito with the id 1 was sold once, id 2 twice, id 3 three times, id 4 four times, and id 5 five times, making the burrito with the id 1 the lowest selling burrito in the array and id 2 the second lowest selling burrito.
