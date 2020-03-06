You must design an efficient (respect time) data structure that can store and check if the total of any three consecutively added element is equal to a given total.

For example, MovingTotal() creates an empty container with no existing totals. The function append([1, 2, 3]) appends [1, 2, 3], that means that there is only one total (1 + 2 + 3 = 6). append([4]) appends element 4 and creates an additional total from the last 3 elements ([2, 3, 4]). Now there would be two totals (1 + 2 + 3 = 6 and 2 + 3 + 4 = 9).
 At this point the function contains(6) and contains(9) should return True, and contains(12) should return False.
