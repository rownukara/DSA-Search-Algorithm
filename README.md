Linear Search
Description:
Linear search is a simple algorithm used to find a specific element in a list or array. It works by checking each element one by one from the beginning to the end of the list until a match is found or the entire list has been searched.

Algorithm:
Start from the first element in the list.
Compare each element with the target value (x).
If an element matches the target value, return its index.
If the end of the list is reached without finding the target, return -1 (indicating the element is not in the list).
Time Complexity:
Best Case: O(1)
(If the target element is at the first position.)
Average Case: O(n)
(On average, the search will go through half of the elements.)
Worst Case: O(n)
(If the target element is not found or is at the last position.)
Space Complexity:
O(1)
(Linear search requires only a constant amount of extra space for variables like the index.)





Binary Search
Description:
Binary search is a more efficient algorithm for finding an element in a sorted list or array. It works by repeatedly dividing the search interval in half. If the value of the target element is less than the middle element, the search continues in the lower half. Otherwise, it continues in the upper half. This process is repeated until the target is found or the interval is empty.

Algorithm:
Start with the entire list and determine the middle element.
If the middle element is the target, return its index.
If the target is smaller than the middle element, search the left half of the list.
If the target is larger than the middle element, search the right half of the list.
Repeat the process until the target is found or the search interval is empty.
Time Complexity:
Best Case: O(1)
(If the target is at the middle of the list in the first comparison.)
Average Case: O(log n)
(With each comparison, the search range is halved.)
Worst Case: O(log n)
(The search continues halving the range until the element is found or the range is empty.)
Space Complexity:
O(1)
(Binary search only requires a constant amount of extra space for variables like low, high, and mid.)
