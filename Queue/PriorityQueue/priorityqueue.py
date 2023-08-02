## implementing priority queue using a list
customer = []
customer.append((1, 'Tejiri'))
customer.append((2, 'Tobi'))
customer.sort(reverse=True)
print(customer)

customer.append((0, 'dami'))
# customer.sort(reverse=True)
customer.append((6, 'Temi'))
customer.sort(reverse=True)
print(customer)

#using heapq to do the priority queue
"""
We can also use the heapq module in Python to implement our priority queue. 
This implementation has O(log n) time for insertion and extraction of the smallest element. 
Note that heapq only has a min heap implementation, but there are other ways to use a max heap
"""
import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
     print(customers)
#Will print names in the order: Riya, Harry, Charles, Stacy.


#
"""
The PriorityQueue uses the same heapq implementation from the previous example internally so it has the same time complexity.
However, it’s different in two key ways. First, it’s synchronized, so it supports concurrent processes. Second, 
it’s a class interface as opposed to the function based interface of heapq. 
Thus, PriorityQueue is the classic object-oriented programming (OOP) style of implementing and using priority queues."""

from queue import PriorityQueue

customer2  =  PriorityQueue()
customer2.put((2, "Harry"))
customer2.put((3, "Charles"))
customer2.put((1, "Riya"))
customer2.put((4, "Stacy"))

while customer2:
    (customer2.get())